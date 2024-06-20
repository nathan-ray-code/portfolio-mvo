import pandas as pd
import pandas_datareader.data as web
import datetime
from functools import reduce
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.efficient_frontier import EfficientFrontier, EfficientCVaR
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt import HRPOpt


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

start = datetime.datetime(2019,9,15)
end = datetime.datetime(2021,9,15)

def get_stock(ticker):
    data = web.DataReader(f"{ticker}", "yahoo", start, end)
    data[f'{ticker}'] = data["Close"]
    data = data[[f'{ticker}']]
    print(data.head())
    return data

# function that creates a dataframe for every individual ticker in a list of tickers
def combine_stocks(tickers):
    data_frames = []
    for i in tickers:
        data_frames.append(get_stock(i))

    df_merged = reduce(lambda left,right: pd.merge(left,right,on=['Data'],how='outer'), data_frames)
    print(df_merged.head())
    return df_merged

"""
MRNA = Moderna (Healthcare)
PFE = (Healthcare)
JNJ = (Healthcare)
GOOGL = (Information Technology)
FB = (Information Technology)
AAPL = (Information Technology)
COST = (Retail)
WMT = (Retail)
KR = (Retail)
JPM = (Financial)
BAC = (Financial)
HSBC = (Financial)

"""

stocks = ["MRNA","PFE","JNJ","GOOGL","FB","AAPL","COST","WMT","KR","JPM","BAC","HSBC"]
combine_returns(stocks)





