import requests
import pandas as pd
import time

def fetch_stock_data(api_key, symbols):
    all_data = []

    for symbol in symbols:
        print(f"Fetching data for {symbol}...")

        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

        response = requests.get(url)
        data = response.json()

        
        if "Time Series (Daily)" not in data:
            print(f"Error fetching {symbol}: {data}")
            continue

        time_series = data["Time Series (Daily)"]
        df = pd.DataFrame.from_dict(time_series, orient='index')

        df['symbol'] = symbol
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'date'}, inplace=True)

        all_data.append(df)

        time.sleep(12)

    final_df = pd.concat(all_data)
    return final_df