import pandas as pd
from assets.check_worksheet import COLS_REQUIRED


def check_cols(df: pd.DataFrame):
    columns = df.columns
    nedded_cols = COLS_REQUIRED.keys()
    types = df.dtypes.to_dict()

    for col in columns:
        if types[col] == COLS_REQUIRED[col]:
            pass
        else:
            print(f"The column {col} does not have a propper typing.")
            break

        if col not in nedded_cols:
            print("The excel sheet does not have the propper columns. Get a standard model in option (#)")
            break

    print("Worksheet read successfully.")
