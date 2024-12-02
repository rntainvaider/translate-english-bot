import psycopg2 as ps
from dotenv import load_dotenv
import os

_ = load_dotenv()

connection = ps.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE"),
)

cursor = connection.cursor()

pr = """
CREATE TABLE words (
    word_id SERIAL PRIMARY KEY,
    word_russian VARCHAR(255) NOT NULL,
    word_translate VARCHAR(255) NOT NULL
    );
"""

cursor.execute(pr)

connection.commit()

cursor.close()
connection.close()
