from database.db_connection import get_connection
from students.student_operations import add_student

connection=get_connection()

if connection:
    print("Connection Test Completed")
    connection.close()