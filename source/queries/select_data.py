import sqlite3
import pandas as pd


def get_indicators(database_path: str) -> list:
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    sql_query = """
            SELECT DISTINCT INDICATOR FROM artemis_project
                """

    cursor.execute(sql_query)
    values = cursor.fetchall()

    output_list = list()
    for row in values:
        output_list.append(row[0])

    print(output_list)
    return output_list

def get_data_of_indicator(database_path: str, indicators_list: list):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    df_output = pd.DataFrame()
    for indicator in indicators_list:
        sql_query = f"""
                SELECT * FROM artemis_project
                WHERE INDICATOR = {indicator}
                    """

        cursor.execute(sql_query)
        values = cursor.fetchall()

        output_list = list()
        for value in values:
            output_list.append(value)

        cols = [
            "INDEX", "KEY", "DATE", "INDICATOR", "VALUE", "STATUS", "INDICATOR_TYPE", 
            "UPDATING_DATE", "UPDATING_MONTH", "UPDATING_YEAR", "SOURCE", 
            "UPDATE_TYPE", "TICKER"
            ]
        df = pd.DataFrame(data=output_list, columns=cols)
        df_output = pd.concat([df_output, df], axis=0)

    return df_output

# get_data_of_indicator("./data/artemis_database.db", ["USD/BRL", "Brent Crude Oil Last Day Financ"])