import yfinance as yf
import pandas as pd
# from tvDatafeed import TvDatafeed


# Getting data from Yahoo Finance
def get_historical_data_from_yf(tickers: list, start_date: str, end_date: str):

    output_df = pd.DataFrame()
    for ticker in tickers:
        try:
            data = yf.download(
                tickers=ticker, 
                start=start_date, 
                end=end_date
                )["Close"].reset_index().rename(
                    columns={"Date":"DATE", "Close":"VALUE"}
                    )

            info = yf.Ticker(ticker).info
            category_name = info.get("shortName")
            indicator_type = info.get("quoteType")
            ticker = info.get("underlyingSymbol")

            data["UPDATING_DATE"] = end_date
            data["INDICATOR"] = category_name
            data["INDICATOR_TYPE"] = indicator_type
            data["STATUS"] = 0
            data["SOURCE"] = "Yahoo Finance"
            data["UPDATE_TYPE"] = 0
            data["TICKER"] = ticker

            output_df = pd.concat([output_df, data], axis=0)
        except:
            print(f"Type a valid ticker! The ticker '{ticker}' is not in the API.")

    return output_df