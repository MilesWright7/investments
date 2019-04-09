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

#stock = 'SPY'
stocks = ['AAP', 'ABT', 'ABBV', 'ACE', 'ACN', 'ADBE', 'ADT', 'AES', 'AET', 'AFL', 'AMG', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'AGN', 'ALXN', 'ALLE', 'ADS', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVGO', 'AVB', 'AVY', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BXLT', 'BAX', 'BBT', 'BDX', 'BBBY', 'BRK-B', 'BBY', 'BLX', 'HRB', 'BA', 'BWA', 'BXP',  'BSK', 'BMY', 'BRCM', 'BF-B', 'CHRW', 'CA', 'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'HSIC', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'GLW', 'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DLPH', 'DAL', 'XRAY', 'DVN', 'DO', 'DTV', 'DFS', 'DISCA', 'DISCK', 'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ENDP', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ES', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FB', 'FAST', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FSIV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GPS', 'GRMN', 'GD', 'GE', 'GGP', 'GIS', 'GM', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOGL', 'GOOG', 'GWW', 'HAL', 'HBI', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCA', 'HCP', 'HCN', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK', 'HUM', 'HBAN', 'ITW', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JEC', 'JBHT', 'JNJ', 'JCI', 'JOY', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'GMCR', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KRFT', 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LM', 'LEG', 'LEN', 'LVLT', 'LUK', 'LLY', 'LNC', 'LLTC', 'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MNK', 'MRO', 'MPC', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MHFI', 'MCK', 'MJN', 'MMV', 'MDT', 'MRK', 'MET', 'KORS', 'MCHP', 'MU', 'MSFT', 'MHK', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NEE', 'NLSN', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO', 'PAYX', 'PNR', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RRC', 'RTN', 'O', 'RHT', 'REGN', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RLC', 'R', 'CRM', 'SNDK', 'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SIAL', 'SPG', 'SWKS', 'SLG', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TE', 'TGNA', 'THC', 'TDC', 'TSO', 'TXN', 'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TJK', 'TMK', 'TSS', 'TSCO', 'RIG', 'TRIP', 'FOXA', 'TSN', 'TYC', 'UA', 'UNP', 'UNH', 'UPS', 'URI', 'UTX', 'UHS', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'ANTM', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WEC', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS']

todays_stocks = ['JPM', 'INTC', 'BA', 'GOOG', 'AMZN']
for stock in todays_stocks:
    starting_cash = 5000
    stock_profit = 0

    CASH = starting_cash
    STOCK_INV = 0



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

        ##real algorithm starts here i guess.
        buy = 'neither'
        if (avg2hr < avg30min) and (avg30min > avg1hr):
            buy = 'buy'
            #buy = 'buy at price ' + str(high)
        elif (avg2hr > avg30min) and (avg30min < avg1hr):
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
