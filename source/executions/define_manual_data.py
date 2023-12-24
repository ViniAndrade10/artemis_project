import pandas as pd


def manual_data_definition(df: pd.DataFrame):
    df["UPDATE_TYPE"] = 1
    df["TICKER"] = ""
    return df