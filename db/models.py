from db.database import get_connection


def init_db() -> None:
    """
    Создает подключение к базе данных
    """

    conn = get_connection()

    with conn.cursor() as cursor:
        cursor.execute(
            """
                       CREATE TABLE IF NOT EXISTS words (
                           word_id SERIAL PRIMARY KEY,
                           word_russian VARCHAR(255) NOT NULL,
                           word_english VARCHAR(255) NOT NULL
                           );
                           """
        )
        conn.commit()
    conn.close


def add_words(word_russian: str, word_english: str) -> None:
    """
    Добавляет новые слова
    """

    conn = get_connection()

    with conn.cursor() as cursor:
        cursor.execute(
            """INSERT INTO words (word_russian, word_english) VALUES (%s, %s)""",
            (word_russian, word_english),
        )
        conn.commit()
    conn.close


def delete_words(word_russian: str) -> None:
    """
    Удаляет слово
    """

    conn = get_connection()

    with conn.cursor() as cursor:
        cursor.execute(
            """DELETE FROM words WHERE word_russian=%s;""",
            (word_russian,),
        )
        conn.commit()
    conn.close


def get_words() -> None:
    """
    Получаем слова
    """

    conn = get_connection()

    with conn.cursor() as cursor:
        cursor.execute("SELECT word_russian, word_english FROM words;")
        result = cursor.fetchall()
    conn.close()

    return result
