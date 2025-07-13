import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_tables(connection):
    create_habits_table = """
    CREATE TABLE IF NOT EXISTS habits (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
    """
    
    create_habit_logs_table = """
    CREATE TABLE IF NOT EXISTS habit_logs (
        habit_id INT,
        log_date DATE,
        status BOOLEAN,
        FOREIGN KEY (habit_id) REFERENCES habits (id)
    );
    """
    
    execute_query(connection, create_habits_table)
    execute_query(connection, create_habit_logs_table)