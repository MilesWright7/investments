"""
Authored by Miles Wright
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
import time
import configparser

config = configparser.ConfigParser()
config.read('credentials.ini')
Key = config['DEFAULT']['key']

#stock = 'SPY'
stocks = ['MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ATVI', 'AYI', 'ADBE', 'AAP', 'AMD', 'AES','AMG', 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALXN', 'ALGN', 'ALLE', 'AGN', 'ADS', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI','ANSS', 'ANTM', 'AON', 'APA', 'AIV', 'AAPL', 'AMAT', 'APTV', 'ADM', 'ARNC', 'AJG', 'AIZ', 'T', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BHGE', 'BLL', 'BAC', 'BAX', 'BBT', 'BDX', 'BRK.B', 'BBY', 'BIIB', 'BLK', 'HRB', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BHF', 'BMY', 'AVGO', 'BF.B', 'CHRW', 'COG', 'CDNS', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CAT', 'CBOE', 'CBRE', 'CBS', 'CELG', 'CNC', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'CXO', 'COP', 'ED', 'STZ', 'GLW', 'COST', 'COTY', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DLR', 'DFS', 'DISCA', 'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DOV', 'DWDP','DTE', 'DUK', 'DRE', 'DXC', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ETR', 'EOG', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'RE', 'ES', 'EXC', 'EXPE', 'EXPD','EXR', 'XOM', 'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FE', 'FISV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FL', 'F', 'FTV', 'FBHS', 'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GD', 'GE','GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GS', 'GT', 'GWW', 'HAL', 'HBI', 'HOG', 'HRS', 'HIG', 'HAS', 'HCA', 'HCP', 'HP', 'HSIC', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HPQ', 'HUM', 'HBAN', 'HII', 'IDXX', 'INFO', 'ITW', 'ILMN', 'INCY', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JBHT', 'JEC', 'SJM', 'JNJ', 'JCI', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KHC', 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LEG', 'LEN','LLY', 'LNC', 'LKQ', 'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MRO', 'MPC', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM','MCHP', 'MU', 'MSFT', 'MAA', 'MHK', 'TAP', 'MDLZ', 'MNST', 'MCO', 'MS', 'MSI', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NKTR', 'NTAP', 'NFLX', 'NWL','NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'PCAR', 'PKG', 'PH', 'PAYX', 'PYPL', 'PNR', 'PBCT', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'RL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'QCOM', 'PWR', 'DGX', 'RRC', 'RJF', 'RTN', 'O', 'RHT', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RHI', 'ROK','ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC','SLB', 'STX', 'SEE', 'SRE', 'SHW', 'SPG', 'SWKS', 'SLG', 'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'SRCL', 'SYK', 'STI', 'SIVB', 'SYMC', 'SYF', 'SNPS', 'SYY', 'TROW', 'TTWO', 'TPR', 'TGT', 'TEL', 'FTI', 'TXN', 'TXT', 'BK', 'CLX', 'COO', 'HSY', 'MOS', 'TRV', 'DIS', 'TMO', 'TIF','TJX', 'TMK', 'TSS', 'TSCO', 'TDG', 'TRIP', 'FOXA', 'FOX', 'TSN', 'USB', 'UDR', 'ULTA', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', 'UTX', 'UHS', 'UNM', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WDC', 'WU', 'WRK', 'WY', 'WHR', 'WMB', 'WLTW', 'WYNN', 'XEL', 'XRX', 'XLNX','XL', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']

todays_stocks = ['JPM', 'INTC', 'BA', 'SPY', 'AMZN']
weed_stocks= ['ASB', 'CGC', 'TLRY', 'CRON', 'APHA']
for stock in todays_stocks:
    starting_cash = 5000
    stock_profit = 0

    CASH = starting_cash
    STOCK_INV = 0



    ts = TimeSeries(key=Key)
    data , meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')


    print('data for stock {}'.format(stock))
    avglist2hr = [None] * 120
    avglist1hr = [None] * 60
    avglist30min = [None] * 30
    avglist15min = [None] * 15

    avg2hr = 0
    avg1hr = 0
    avg30min = 0
    avg15min = 0

    for date in sorted(data):
        dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        high = float(data[date]['2. high'])
        minute = int(dt.strftime("%M"))
        hour = int(dt.strftime("%H"))
        mod2hr = (minute + 60*hour) % 120
        mod1hr = minute % 60
        mod30min = minute % 30
        mod15min = minute % 15

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

        avglist15min[mod15min] = high
        sum = 0
        counter = 1
        for entry in avglist15min:
            if entry != None:
                if sum != 0:
                    counter += 1
                sum += entry
        avg15min = sum/counter

        ##real algorithm starts here i guess.
        buy = 'neither'
        if (avg1hr < avg15min) and (avg15min > avg30min):
            buy = 'buy'
            #buy = 'buy at price ' + str(high)
        elif (avg1hr < avg15min) and (avg15min < avg30min):
            buy = 'sell'
            #buy = 'sell at price ' + str(high)


            ##testing profit
        if buy == 'buy' and CASH > high and 10 < int(dt.strftime("%H")):
            while CASH > high:
                CASH -= high
                STOCK_INV += 1
                profit = high * STOCK_INV + CASH - starting_cash
            print('{0} {1} at {2:.2f}\t\tNet profit of ${3:.2f} \tAPR {4}\n'.format(buy, STOCK_INV, high, profit, dt.strftime("%d, %H:%M:%S")))

        elif buy == 'sell' and STOCK_INV > 0:
            while STOCK_INV > 0:
                STOCK_INV -= 1
                CASH += high
                profit = high * STOCK_INV + CASH - starting_cash
            print('{0} all at {1:.2f}\t\tNet profit of ${2:.2f} \tAPR {3}'.format(buy, high, profit, dt.strftime("%d, %H:%M:%S")))

        if dt.strftime("%Y-%m-%d %H:%M:%S") == '2019-04-08 16:00:00':
            stock_profit = high * STOCK_INV + CASH - starting_cash

    print("profit for stock {0} was {1:.2f}".format(stock, stock_profit))
    #time.sleep(10)
#           print("{0}:\t 30min avg: {1:.2f}\t1hr avg: {2:.2f}\t2hr avg: {3:.2f}\t {4}".format(date, avg30min, avg1hr, avg2hr, buy))
