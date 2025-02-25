from pydantic import BaseModel, create_model, EmailStr
from database import metadata

# Dictionary to store dynamically generated Pydantic models
schemas = {}

for table_name, table in metadata.tables.items():
    fields = {}
    for column in table.columns:
        field_type = str  # Default to string
        if column.type.python_type == int:
            field_type = int
        elif column.type.python_type == float:
            field_type = float
        elif column.type.python_type == bool:
            field_type = bool

        fields[column.name] = (field_type, ...)

    # Create Pydantic model dynamically
    schemas[table_name] = create_model(f"{table_name.capitalize()}Schema", **fields)
