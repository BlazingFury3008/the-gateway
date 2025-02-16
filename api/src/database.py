import mysql.connector
from dotenv import load_dotenv
from contextlib import contextmanager
import os

# Load environment variables
load_dotenv()

# MySQL Credentials
db_host = os.getenv('DB_HOST', '92.205.5.205')
db_user = os.getenv('DB_USER', 'aiden')
db_password = os.getenv('DB_PASSWORD', 'Dasher123@bc')
db_database = os.getenv('DB_DATABASE', 'theGateway')

# Get MySQL Connection
def get_mysql_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )

# Dependency for MySQL
@contextmanager
def get_mysql_db():
    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)  # Returns results as dictionaries
    try:
        yield connection, cursor
    finally:
        cursor.close()
        connection.close()
