import pandas as pd

def transform_data(df):
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'symbol']

    df['date'] = pd.to_datetime(df['date'])

    for col in ['open', 'high', 'low', 'close', 'volume']:
        df[col] = df[col].astype(float)

    df = df.sort_values(by=['symbol', 'date'])

    # Feature Engineering
    df['daily_return'] = (df['close'] - df['open']) / df['open']

    df['ma_7'] = df.groupby('symbol')['close'].transform(lambda x: x.rolling(7).mean())
    df['ma_30'] = df.groupby('symbol')['close'].transform(lambda x: x.rolling(30).mean())

    df['volatility'] = df.groupby('symbol')['daily_return'].transform(lambda x: x.rolling(7).std())

    return df