import sqlite3
from sqlite3 import Error

DB_PATH = 'christmas.db'

def create_connection():
    try:
        return sqlite3.connect(DB_PATH)
    except Error as e:
        print(f"Error creating connection: {e}")
        return None

def execute_query(query, params=(), fetch=False, commit=False):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            if commit:
                conn.commit()
            if fetch:
                return cursor.fetchall()
            return True
        except Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            conn.close()

def insert_user(username: str, password: str, email: str):
    query = "INSERT INTO users (username, password, email, is_naughty) VALUES (?, ?, ?, True)"
    return execute_query(query, (username, password, email), commit=True)

def login_user(username: str, password: str):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    users = execute_query(query, (username, password), fetch=True)
    return users[0] if users else None

def list_user(identifier: int):
    query = "SELECT * FROM users WHERE id=?"
    users = execute_query(query, (identifier,), fetch=True)
    return users[0] if users else None

def list_gifts():
    query = "SELECT * FROM presents"
    gifts = execute_query(query, fetch=True)
    return gifts

def update_user(column, value, username: str):
    query = f"UPDATE users SET {column} = ? WHERE username = ?"
    return execute_query(query, (value, username), commit=True)

def check_password(old_password: str):
    query = f"SELECT password from {column} = ? WHERE id = ?"
    return execute_query(query, (value, id_value), fetch=True)

def check_column(column: str):
    query = f"SELECT ? from users"
    return execute_query(query, (column,), fetch=True)

def check_naughty(username: str):
    query = f"SELECT is_naughty FROM users WHERE username=?"
    admin = execute_query(query, (username,), fetch=True)
    return admin[0][0] if admin else None
