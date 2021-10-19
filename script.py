from csv import DictReader, DictWriter
import pandas as pd



df =pd.read_csv('OHLC.csv')
df['Volume'] = df['Volume'].str.replace(',', '').astype(int)
# print(df)
df.to_csv('ALLdata.csv')



























        