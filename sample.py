"""
using https://www.alphavantage.co/documentation/ as a live stock api
and pandas for printing pretty kinda use output_format='pandas' in ts call
and use pprint for print statement
https://www.programiz.com/python-programming/datetime/strptime
date and time useage
"""


from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import json
from datetime import datetime

stock = 'GOOGL'

ts = TimeSeries(key="EDO4E7F3ZCJ4299H")
data , meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')


print('data for stock {}'.format(stock))
avglist2hr = [None] * 120
avglist1hr = [None] * 60
avglist30min = [None] * 30

avg2hr = 0
avg1hr = 0
avg30min = 0
for date in sorted(data):
    dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    high = float(data[date]['2. high'])
    minute = int(dt.strftime("%M"))
    hour = int(dt.strftime("%H"))
    mod2hr = (minute + 60*hour) % 120
    mod1hr = minute % 60
    mod30min = minute % 30

    #2 hr average calculation
    avglist2hr[mod2hr] = high
    sum = 0
    counter = 1
    for entry in avglist2hr:
        if entry != None:
            if sum != 0:
                counter += 1
            sum += entry
    avg2hr = sum/counter

    #1 hr average calculation
    avglist1hr[mod1hr] = high
    sum = 0
    counter = 1
    for entry in avglist1hr:
        if entry != None:
            if sum != 0:
                counter += 1
            sum += entry
    avg1hr = sum/counter

    #30 min average calculation
    avglist30min[mod30min] = high
    sum = 0
    counter = 1
    for entry in avglist30min:
        if entry != None:
            if sum != 0:
                counter += 1
            sum += entry
    avg30min = sum/counter


    print("30min avg: {0:.2f}\t1hr avg: {1:.2f}\t2hr avg: {2:.2f}".format(avg30min, avg1hr, avg2hr))
