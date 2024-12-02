import psycopg2 as ps
from dotenv import load_dotenv
import os

_ = load_dotenv()


def get_connection():
    connection = ps.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE"),
    )
    return connection
