import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL server host if different
            user='root',       # Replace with your MySQL username
            password='yourpassword'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database with IF NOT EXISTS
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:  # Catching specific mysql.connector errors
        print(f"Error: '{err}' occurred while connecting to MySQL server")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
