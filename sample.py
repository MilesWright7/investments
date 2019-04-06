"""
using https://www.alphavantage.co/documentation/ as a live stock api
and pandas for printing pretty kinda use output_format='pandas' in ts call
and use pprint for print statement
"""


from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import json

stock = 'SPY'

ts = TimeSeries(key="EDO4E7F3ZCJ4299H")
data , meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='compact')



print('data for stock {}'.format(stock))
for key in data:
    print(data[key])
print(data)
