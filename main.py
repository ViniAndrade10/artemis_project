import pandas as pd
from source.executions.get_historical_data import get_historical_data_from_yf
from source.prompt.prompt_execution import add_new_tickers
from source.queries.insert_data import insert_data_into_database
from assets.dates import start_date, end_date
from assets.path import database_path


print("Welcome to the Artemis Project interface.\n")
print("1 - Get historical data of Stock Market.")

value = input("Select your option: ")

if value == 1 or value == "1":
    ticker_list = add_new_tickers()
    df = get_historical_data_from_yf(ticker_list, start_date, end_date)
    insert_data_into_database(database_path, df)
