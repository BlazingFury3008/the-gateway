from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from database import get_db, metadata
from schemas import schemas
from auth_utils import validate_api_key  # Import API Key Validator

# Tables to exclude from the API
EXCLUDED_TABLES = {"api_keys", "admin_logs"}  # Add any tables you want to exclude

router = APIRouter()

def create_table_routes(table_name: str, table):
    """
    Dynamically creates API routes for a given table.
    Captures the table_name in a function to avoid loop variable scoping issues.
    """
    ModelSchema = schemas.get(table_name)
    if not ModelSchema:
        print(f"Warning: No schema found for table '{table_name}', skipping...")
        return

    primary_keys = table.primary_key.columns.keys()
    if not primary_keys:
        print(f"Warning: Table '{table_name}' has no primary key. Skipping...")
        return

    primary_key = primary_keys[0]  # Use the first primary key

    # Get table comment to use as a tag
    table_tag = table.comment if table.comment else "General"
    print(f"Registering table: {table_name} | Tag: {table_tag}")

    @router.post(f"/data/{table_name}/", response_model=ModelSchema, dependencies=[Depends(validate_api_key)], tags=[table_tag])
    async def create_entry(data: ModelSchema, db: Session = Depends(get_db)):
        """
        Creates a new record in the {table_name} table.
        """
        insert_stmt = table.insert().values(**data.dict())
        db.execute(insert_stmt)
        db.commit()
        return data

    @router.get(f"/data/{table_name}/", response_model=list[ModelSchema],dependencies=[Depends(validate_api_key)],  tags=[table_tag])
    async def get_all_entries(db: Session = Depends(get_db)):
        """
        Retrieves all records from the {table_name} table.
        """
        result = db.execute(select(table)).fetchall()
        return [dict(row._mapping) for row in result]  # Convert results to dictionaries

    @router.get(f"/data/{table_name}/{{id}}", response_model=ModelSchema, dependencies=[Depends(validate_api_key)], tags=[table_tag])
    async def get_entry_by_id(id: int, db: Session = Depends(get_db)):
        """
        Retrieves a specific record from the {table_name} table using the primary key.
        """
        result = db.execute(select(table).where(table.c[primary_key] == id)).first()
        if not result:
            raise HTTPException(status_code=404, detail=f"{table_name} record not found")
        return result

    @router.put(f"/data/{table_name}/{{id}}", response_model=ModelSchema, dependencies=[Depends(validate_api_key)], tags=[table_tag])
    async def update_entry(id: int, data: ModelSchema, db: Session = Depends(get_db)):
        """
        Updates a specific record in the {table_name} table using the primary key.
        """
        update_stmt = table.update().where(table.c[primary_key] == id).values(**data.dict())
        db.execute(update_stmt)
        db.commit()
        return data

    @router.delete(f"/data/{table_name}/{{id}}", dependencies=[Depends(validate_api_key)], tags=[table_tag])
    async def delete_entry(id: int, db: Session = Depends(get_db)):
        """
        Deletes a specific record from the {table_name} table using the primary key.
        """
        delete_stmt = table.delete().where(table.c[primary_key] == id)
        db.execute(delete_stmt)
        db.commit()
        return {"message": f"{table_name} record with {primary_key}={id} deleted successfully"}

# Register routes dynamically
for table_name, table in metadata.tables.items():
    if table_name in EXCLUDED_TABLES:
        print(f"🛑 Skipping excluded table: {table_name}")
        continue
    create_table_routes(table_name, table)

print("API routes generated dynamically with tags from table comments.")
