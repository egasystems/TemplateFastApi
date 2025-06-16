import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
from dotenv import load_dotenv
import os

load_dotenv()
# Aquí colocas tu configuración real
DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASS"),
    'database': os.getenv("DB_NAME")
}

@contextmanager
def get_connection():
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        yield conn
    except Error as e:
        print(f"DB Error: {e}")
        raise
    finally:
        if conn and conn.is_connected():
            conn.close()