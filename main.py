# type: ignore

import pandas as pd
from source.executions.get_historical_data import get_historical_data_from_yf
from source.prompt.prompt_execution import add_new_tickers, select_file, add_indicators
from source.queries.insert_data import insert_data_into_database
from source.queries.select_data import get_data_of_indicator, get_indicators
from source.queries.select_tickers import ticker_selection
from source.prompt.check_excel import check_cols
from assets.dates import start_date, end_date
from assets.path import database_path


print("\nWelcome to the Artemis Project interface.\n")
print("1 - Get historical data of Stock Market.")
print("2 - Input data manually.")
print("3 - Update rolling forecast.")
print("4 - Data extraction.")

value = input("Select your option: ")

if value == 1 or value == "1":
    ticker_list = add_new_tickers()
    df = get_historical_data_from_yf(ticker_list, start_date, end_date)
    insert_data_into_database(database_path, df)

elif value == 2 or value == "2":
    df = select_file()
    check_cols(df)
    insert_data_into_database(database_path, df)

elif value == 3 or value == "3":
    tickers = ticker_selection(database_path)
    for ticker, last_date in tickers.items():
        df = get_historical_data_from_yf([ticker], str(last_date).split(" ")[0], end_date)
        insert_data_into_database(database_path, df)
        print(df)

elif value == 4 or value == "4":
    response = input("Would you like to get the names of the indicators? [y / n]")
    if response.lower() == "n" or response.lower() == "no":
        pass
    elif response.lower() == "y" or response.lower() == "yes":
        _ = get_indicators(database_path)
    else:
        print("Type a correct responde!")

    indicators_list = add_indicators()
    df = get_data_of_indicator(database_path, indicators_list)
    print(df)