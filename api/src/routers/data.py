from fastapi import APIRouter, Depends, HTTPException, Body
from database import get_mysql_db

router = APIRouter(tags=["Database"])

### 🛠 LIST TABLES ###
@router.get("/tables")
def list_tables():
    """List all tables in the database using MySQL Connector."""
    try:
        with get_mysql_db() as (conn, cursor):
            cursor.execute("SHOW TABLES")
            tables = [list(row.values())[0] for row in cursor.fetchall()]
        return {"tables": tables}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


### 🛠 CREATE TABLE ###
@router.post("/tables")
def create_table(table_name: str = Body(...), columns: dict = Body(...)):
    """
    Create a new table.
    Expects `columns` as a dictionary of column names and SQL data types.
    """
    try:
        column_definitions = ", ".join([f"`{col}` {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE `{table_name}` ({column_definitions});"

        with get_mysql_db() as (conn, cursor):
            cursor.execute(query)
            conn.commit()
        
        return {"message": f"Table `{table_name}` created successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating table: {str(e)}")


### 🛠 DELETE TABLE ###
@router.delete("/tables/{table_name}")
def delete_table(table_name: str):
    """Delete a table from the database"""
    try:
        with get_mysql_db() as (conn, cursor):
            cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`;")
            conn.commit()
        return {"message": f"Table `{table_name}` deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting table: {str(e)}")


### 🛠 RETRIEVE DATA FROM TABLE ###
@router.get("/tables/{table_name}")
def get_table_data(table_name: str):
    """Retrieve all rows & column types from a table"""
    try:
        with get_mysql_db() as (conn, cursor):
            cursor.execute(f"SHOW COLUMNS FROM `{table_name}`")
            column_types = {row["Field"]: row["Type"] for row in cursor.fetchall()}  

            cursor.execute(f"SELECT * FROM `{table_name}`")
            data = cursor.fetchall()
        
        return {"data": data, "column_types": column_types}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving table data: {str(e)}")


### 🛠 INSERT DATA INTO TABLE ###
@router.post("/tables/{table_name}/insert")
def insert_into_table(table_name: str, row_data: dict = Body(...)):
    """Insert data into a table."""
    try:
        columns = ", ".join([f"`{key}`" for key in row_data.keys()])
        values = ", ".join(["%s" for _ in row_data.values()])
        query = f"INSERT INTO `{table_name}` ({columns}) VALUES ({values})"

        with get_mysql_db() as (conn, cursor):
            cursor.execute(query, tuple(row_data.values()))
            conn.commit()
        
        return {"message": "Data inserted successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error inserting data: {str(e)}")


### 🛠 UPDATE DATA IN TABLE ###
@router.put("/tables/{table_name}/update")
def update_table_data(table_name: str, conditions: dict = Body(...), updates: dict = Body(...)):
    """Update records in a table based on conditions."""
    try:
        set_clause = ", ".join([f"`{key}` = %s" for key in updates.keys()])
        where_clause = " AND ".join([f"`{key}` = %s" for key in conditions.keys()])
        query = f"UPDATE `{table_name}` SET {set_clause} WHERE {where_clause}"

        with get_mysql_db() as (conn, cursor):
            cursor.execute(query, tuple(updates.values()) + tuple(conditions.values()))
            conn.commit()

        return {"message": "Data updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating table: {str(e)}")


### 🛠 DELETE DATA FROM TABLE ###
@router.delete("/tables/{table_name}/delete")
def delete_from_table(table_name: str, conditions: dict = Body(...)):
    """Delete records from a table based on conditions."""
    try:
        where_clause = " AND ".join([f"`{key}` = %s" for key in conditions.keys()])
        query = f"DELETE FROM `{table_name}` WHERE {where_clause}"

        with get_mysql_db() as (conn, cursor):
            cursor.execute(query, tuple(conditions.values()))
            conn.commit()
        
        return {"message": "Data deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting data: {str(e)}")


### 🛠 EXECUTE RAW SQL QUERY ###
@router.post("/execute")
def execute_sql(query: str = Body(...)):
    """Execute a raw SQL command"""
    try:
        with get_mysql_db() as (conn, cursor):
            cursor.execute(query)

            if query.strip().lower().startswith("select"):
                return {"results": cursor.fetchall()}

            conn.commit()
            return {"message": "Query executed successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"SQL Execution Error: {str(e)}")
