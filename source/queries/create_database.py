import sqlite3

from pathlib import Path
import os


def create_database(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    sql_query = """
                CREATE TABLE IF NOT EXISTS artemis_project (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                KEY VARCHAR(255),
                DATE DATETIME,
                INDICATOR VARCHAR,
                VALUE FLOAT, 
                STATUS INTEGER,
                INDICATOR_TYPE VARCHAR,
                UPDATING_DATE DATETIME,
                UPDATING_MONTH INTEGER,
                UPDATING_YEAR INTEGER,
                SOURCE VARCHAR,
                UPDATE_TYPE INTEGER,
                TICKER VARCHAR
                );
                """

    cursor.execute(sql_query)
    conn.commit()
    conn.close()


if __name__=="__main__":
    __ROOT_PATH__ = Path(__file__).resolve().parent.parent
    # database_path = os.path.join(__ROOT_PATH__, "data", "artemis_database.db")
    # create_database(database_path)
    database_path = os.path.join(".", "data", "artemis_database.db")
    create_database(database_path)
