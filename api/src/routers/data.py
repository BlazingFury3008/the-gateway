from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from sqlalchemy import text, exc
from database import get_db

router = APIRouter(tags=["Database"])

### 🛠 LIST TABLES ###
@router.get("/tables")
def list_tables(db: Session = Depends(get_db)):
    """List all tables in the database"""
    try:
        result = db.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result.fetchall()]
        return {"tables": tables}
    except exc.SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


### 🛠 CREATE TABLE ###
@router.post("/tables")
def create_table(table_name: str = Body(...), columns: dict = Body(...), db: Session = Depends(get_db)):
    """
    Create a new table.
    Expects `columns` as a dictionary of column names and SQL data types.
    Example:
    {
        "table_name": "users",
        "columns": {
            "id": "INT PRIMARY KEY AUTO_INCREMENT",
            "name": "VARCHAR(100) NOT NULL",
            "email": "VARCHAR(100) UNIQUE NOT NULL"
        }
    }
    """
    try:
        column_definitions = ", ".join([f"`{col}` {dtype}" for col, dtype in columns.items()])
        query = text(f"CREATE TABLE `{table_name}` ({column_definitions});")
        db.execute(query)
        db.commit()
        return {"message": f"Table `{table_name}` created successfully"}
    
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


### 🛠 DELETE TABLE ###
@router.delete("/tables/{table_name}")
def delete_table(table_name: str, db: Session = Depends(get_db)):
    """Delete a table from the database"""
    try:
        db.execute(text(f"DROP TABLE `{table_name}`;"))
        db.commit()
        return {"message": f"Table `{table_name}` deleted successfully"}
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


### 🛠 RETRIEVE DATA FROM TABLE ###
@router.get("/tables/{table_name}")
def get_table_data(table_name: str, db: Session = Depends(get_db)):
    """Retrieve all rows & column types from a table"""
    result = db.execute(text(f"SHOW COLUMNS FROM `{table_name}`"))
    column_types = {row[0]: row[1] for row in result.fetchall()}  # Fetch column types
    
    data = db.execute(text(f"SELECT * FROM `{table_name}`")).mappings().all()
    
    return {"data": data, "column_types": column_types}



### 🛠 INSERT DATA INTO TABLE ###
@router.post("/tables/{table_name}/insert")
def insert_into_table(table_name: str, row_data: dict = Body(...), db: Session = Depends(get_db)):
    """
    Insert data into a table.
    Example:
    {
        "name": "John Doe",
        "email": "johndoe@example.com"
    }
    """
    try:
        columns = ", ".join([f"`{key}`" for key in row_data.keys()])
        values = ", ".join([f":{key}" for key in row_data.keys()])
        query = text(f"INSERT INTO `{table_name}` ({columns}) VALUES ({values});")
        db.execute(query, row_data)
        db.commit()
        return {"message": "Data inserted successfully"}
    
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


### 🛠 UPDATE DATA IN TABLE ###
@router.put("/tables/{table_name}/update")
def update_table_data(table_name: str, conditions: dict = Body(...), updates: dict = Body(...), db: Session = Depends(get_db)):
    """
    Update records in a table based on conditions.
    Example:
    {
        "conditions": {"id": 1},
        "updates": {"name": "Jane Doe"}
    }
    """
    try:
        condition_str = " AND ".join([f"`{key}` = :{key}" for key in conditions.keys()])
        update_str = ", ".join([f"`{key}` = :{key}" for key in updates.keys()])

        query = text(f"UPDATE `{table_name}` SET {update_str} WHERE {condition_str};")
        db.execute(query, {**updates, **conditions})
        db.commit()

        return {"message": "Data updated successfully"}
    
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


### 🛠 DELETE DATA FROM TABLE ###
@router.delete("/tables/{table_name}/delete")
def delete_from_table(table_name: str, conditions: dict = Body(...), db: Session = Depends(get_db)):
    """
    Delete records from a table based on conditions.
    Example:
    {
        "conditions": {"id": 1}
    }
    """
    try:
        condition_str = " AND ".join([f"`{key}` = :{key}" for key in conditions.keys()])
        query = text(f"DELETE FROM `{table_name}` WHERE {condition_str};")
        db.execute(query, conditions)
        db.commit()
        return {"message": "Data deleted successfully"}
    
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


### 🛠 EXECUTE RAW SQL QUERY ###
@router.post("/execute")
def execute_sql(query: str = Body(...), db: Session = Depends(get_db)):
    """Execute a raw SQL command"""
    try:
        result = db.execute(text(query))

        # Return data only for SELECT queries
        if query.strip().lower().startswith("select"):
            return {"results": [dict(row) for row in result.mappings()]}

        db.commit()
        return {"message": "Query executed successfully"}

    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
