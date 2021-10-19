import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from nepse_recomand import nepse_live_data

data = nepse_live_data()
# print(data)
sn=[]
stock_id=[]
stock_symbol=[]
max_price=[]
min_price=[]
closing_price=[]
traded_shares=[]
previous_closing=[]
percent_difference=[]
date=[]

for i,live_data in enumerate(data['live']):
    sn.append(i+1)
    stock_id.append(live_data["StockID"])
    stock_symbol.append(live_data["StockSymbol"])
    max_price.append(live_data["MaxPrice"])
    min_price.append(live_data["MinPrice"])
    closing_price.append(live_data["ClosingPrice"])
    traded_shares.append(live_data["TradedShares"])
    previous_closing.append(live_data["PreviousClosing"])
    percent_difference.append(live_data["PercentDifference"])
    date.append(live_data["Date"])
    # nepse_values.append([i+1,live_data["StockID"],live_data["StockSymbol"],live_data["MaxPrice"],live_data["MinPrice"],live_data["ClosingPrice"],live_data["TradedShares"],live_data["PreviousClosing"],live_data["PercentDifference"],live_data["Date"]])
    

fig = go.Figure(data=[go.Table(header=dict(values=['S.N', 'Stock ID','Stock Symbol','Max Price','Min Price','Closing Price','Traded Shares','Previous Closing','Percent Difference','Date']),
                 cells=dict(values=[sn,stock_id,stock_symbol,max_price,min_price,closing_price,traded_shares,previous_closing,percent_difference,date]))
                     ])
fig.show()