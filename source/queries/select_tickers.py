import sqlite3


def ticker_selection(database_path: str):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    sql_query = f"""
    SELECT TICKER, MAX(DATE) AS data_maxima
    FROM artemis_project
    GROUP BY TICKER;
"""

    cursor.execute(sql_query)
    values = cursor.fetchall()

    output_value = dict()
    for value in values:
        output_value[value[0]] = value[1]

    return output_value
