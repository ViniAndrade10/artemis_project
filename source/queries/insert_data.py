import sqlite3
import pandas as pd


def make_keys(df: pd.DataFrame):
    df["UPDATING_DATE"] = pd.to_datetime(df["UPDATING_DATE"])
    df["UPDATING_MONTH"] = [str(int(mes)) for mes in df["UPDATING_DATE"].dt.month]
    df["UPDATING_YEAR"] = [str(int(year)) for year in df["UPDATING_DATE"].dt.year]
    df["DATE"] = [str(date) for date in df["DATE"]]

    df["KEY"] = df["DATE"]+ "_" + df["INDICATOR"] + "_" +df["UPDATING_MONTH"] + "_" + df["UPDATING_YEAR"]
    df["DATE"] = pd.to_datetime(df["DATE"])
    return df


def insert_data_into_database(database_path: str, df: pd.DataFrame):
    conn = sqlite3.connect(database_path)
    df = make_keys(df)
    df.to_sql("artemis_project", con=conn, index=False, if_exists="append")
    print("Data inputed successfully.")
