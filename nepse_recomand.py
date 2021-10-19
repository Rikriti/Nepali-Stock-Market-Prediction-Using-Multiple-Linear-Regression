import os

import requests
import json
from datetime import date


def nepse_live_data(symbol=None):
    response = requests.get("https://api.sheezh.com/nepse/v1/live", params={"symbol": symbol})
    return response.json()


def nepse_data_dump():
    today = date.today()
    file_name = "trading_data/" + today.strftime("%Y-%m-%d") + ".json"
    # print(file_name)
    with open(file_name, "w") as f:
        json.dump(nepse_live_data(), f)


def stock_recommender(trading_files="trading_data"):
    average_stock_percent_diff = {}
    for subdir, dirs, files in os.walk(trading_files):
        dated_stock_percent_diff = {}
        for file in files:
            stock_json_file = os.path.join(subdir, file)
            with open(stock_json_file, "r") as f:
                stock_json = json.load(f)
            for stock_date_data in stock_json['live']:
                dated_stock_percent_diff[stock_date_data["StockSymbol"]] = stock_date_data['PercentDifference']
            for k, v in dated_stock_percent_diff.items():
                average_stock_percent_diff[k] = (average_stock_percent_diff.get(k, 0) + float(v)) / len(files)
    max_stock_symbol = max(average_stock_percent_diff, key=average_stock_percent_diff.get)
    return max_stock_symbol


if __name__ == '__main__':
    nepse_data_dump()
    print(stock_recommender())
