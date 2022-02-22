# coding=utf-8
import csv
import cbpro
import urllib.request
import pandas
import matplotlib.pyplot as pyplot
from stockstats import StockDataFrame
from datetime import datetime
import os

REALTIME = datetime.now()

os.system("cls")
os.system("color a")


InputLog = str(input("\n Type The Name Of Your Chosen Coin : "))

InputLog = InputLog.upper()


if (InputLog == "ETH"):
    LOG_FILE = open("./Base/LOG.csv", "w", encoding='UTF8')
    Import = (f'\n İşlem Saati=>  {REALTIME} \n Seçilen Coin= > ' + InputLog)
    LOG_FILE.write(Import)

    public_client = cbpro.PublicClient()

    RealTimeValueBase = public_client.get_product_24hr_stats(f'{InputLog}-USD')
    Param = ['open', 'high', 'low', 'volume', 'last', 'volume_30day']

    Matris = []
    Matris.append(RealTimeValueBase)

    DataTimer = open('CoinValue.csv', 'w', encoding='UTF8')

    Encoder = csv.writer(DataTimer)

    row = Matris[0:10]

    Encoder.writerow(row)

    RealFrame = pandas.read_csv('CoinValue.csv', 'w', names=Param)
    stock = StockDataFrame.retype(RealFrame)

    print(Matris)

    DataTimer.close()

    InputLog_2 = str(
        input("\n Write The Name Of The Indicator You Have Chosen : "))
    InputLog_2 = InputLog_2.lower()

    Coin_Optioner = InputLog
    Currency_Optioner = "USDT"
    Coin = str((Coin_Optioner + Currency_Optioner))

    url = 'https://www.binance.com/api/v1/klines?symbol=' + Coin + '&interval=1d'
    names = ['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'Quoteassetvolume',
             'Numberoftrades', 'Takerbuybaseassetvolume', 'Takerbuyquoteassetvolume', 'Ignore']
    response = urllib.request.urlopen(url)

    df = pandas.read_json(response.read())

    # We will save this captured data to the computer.
    df.to_csv('BinanceData.csv', encoding='utf-8', index=False, header=False)

    # The recorded data will be graphed
    dataframe = pandas.read_csv('BinanceData.csv', names=names)

    # Calculations such as MACD SMA RSI will be made.
    stock = StockDataFrame.retype(dataframe)

    rsi12 = stock[InputLog_2]
    dataframe.opentime = pandas.to_datetime(dataframe.opentime, unit='ms')

    pyplot.subplot(211)
    pyplot.title(f'{Coin_Optioner} - {Currency_Optioner}')
    pyplot.plot(dataframe.opentime, dataframe.close)
    # The graph will be added to these calculations.
    pyplot.subplot(212)
    pyplot.title(f'{InputLog_2} - Indicator')
    pyplot.plot(dataframe.opentime, rsi12)
    pyplot.show()

if (InputLog == "DOGE"):

    File = open('CoinBaseDays.csv', 'w', encoding='UTF8')

    InputLog_2 = str(

        input("\n Write The Name Of The Indicator You Have Chosen : "))

    InputLog_2 = InputLog_2.lower()

    Coin_Optioner = InputLog

    Currency_Optioner = "USDT"

    Coin = str((Coin_Optioner + Currency_Optioner))

    url = 'https://www.binance.com/api/v1/klines?symbol=' + Coin + '&interval=1d'
    names = ['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'Quoteassetvolume',
             'Numberoftrades', 'Takerbuybaseassetvolume', 'Takerbuyquoteassetvolume', 'Ignore']
    response = urllib.request.urlopen(url)

    df = pandas.read_json(response.read())

    # We will save this captured data to the computer.
    df.to_csv('BinanceData.csv', encoding='utf-8', index=False, header=False)

    # The recorded data will be graphed
    dataframe = pandas.read_csv('BinanceData.csv', names=names)

    # Calculations such as MACD SMA RSI will be made.
    stock = StockDataFrame.retype(dataframe)

    rsi12 = stock[InputLog_2]
    dataframe.opentime = pandas.to_datetime(dataframe.opentime, unit='ms')

    pyplot.subplot(211)
    pyplot.title(f'{Coin_Optioner} - {Currency_Optioner}')
    pyplot.plot(dataframe.opentime, dataframe.close)
    # The graph will be added to these calculations.
    pyplot.subplot(212)
    pyplot.title(f'{InputLog_2} - Indicator')
    pyplot.plot(dataframe.opentime, rsi12)
    pyplot.show()

if (InputLog == "BNB"):
    InputLog_2 = str(
        input("\n Write The Name Of The Indicator You Have Chosen : "))
    InputLog_2 = InputLog_2.lower()

    Coin_Optioner = InputLog
    Currency_Optioner = "USDT"
    Coin = str((Coin_Optioner + Currency_Optioner))

    url = 'https://www.binance.com/api/v1/klines?symbol=' + Coin + '&interval=1d'
    names = ['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'Quoteassetvolume',
             'Numberoftrades', 'Takerbuybaseassetvolume', 'Takerbuyquoteassetvolume', 'Ignore']
    response = urllib.request.urlopen(url)

    df = pandas.read_json(response.read())

    # We will save this captured data to the computer.
    df.to_csv('BinanceData.csv', encoding='utf-8', index=False, header=False)

    # The recorded data will be graphed
    dataframe = pandas.read_csv('BinanceData.csv', names=names)

    # Calculations such as MACD SMA RSI will be made.
    stock = StockDataFrame.retype(dataframe)

    rsi12 = stock[InputLog_2]
    dataframe.opentime = pandas.to_datetime(dataframe.opentime, unit='ms')

    pyplot.subplot(211)
    pyplot.title(f'{Coin_Optioner} - {Currency_Optioner}')
    pyplot.plot(dataframe.opentime, dataframe.close)
    # The graph will be added to these calculations.
    pyplot.subplot(212)
    pyplot.title(f'{InputLog_2} - Indicator')
    pyplot.plot(dataframe.opentime, rsi12)
    pyplot.show()

if (InputLog == "BTC"):
    InputLog_2 = str(
        input("\n Write The Name Of The Indicator You Have Chosen : "))
    InputLog_2 = InputLog_2.lower()

    Coin_Optioner = InputLog
    Currency_Optioner = "USDT"
    Coin = str((Coin_Optioner + Currency_Optioner))

    url = 'https://www.binance.com/api/v1/klines?symbol=' + Coin + '&interval=1d'
    names = ['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'Quoteassetvolume',
             'Numberoftrades', 'Takerbuybaseassetvolume', 'Takerbuyquoteassetvolume', 'Ignore']
    response = urllib.request.urlopen(url)

    df = pandas.read_json(response.read())

    # We will save this captured data to the computer.
    df.to_csv('BinanceData.csv', encoding='utf-8', index=False, header=False)

    # The recorded data will be graphed
    dataframe = pandas.read_csv('BinanceData.csv', names=names)

    # Calculations such as MACD SMA RSI will be made.
    stock = StockDataFrame.retype(dataframe)

    rsi12 = stock[InputLog_2]
    dataframe.opentime = pandas.to_datetime(dataframe.opentime, unit='ms')

    pyplot.subplot(211)
    pyplot.title(f'{Coin_Optioner} - {Currency_Optioner}')
    pyplot.plot(dataframe.opentime, dataframe.close)
    # The graph will be added to these calculations.
    pyplot.subplot(212)
    pyplot.title(f'{InputLog_2} - Indicator')
    pyplot.plot(dataframe.opentime, rsi12)
    pyplot.show()

if (InputLog == "BNB"):
    InputLog_2 = str(
        input("\n Write The Name Of The Indicator You Have Chosen : "))
    InputLog_2 = InputLog_2.lower()

    Coin_Optioner = InputLog
    Currency_Optioner = "USDT"
    Coin = str((Coin_Optioner + Currency_Optioner))

    url = 'https://www.binance.com/api/v1/klines?symbol=' + Coin + '&interval=1d'
    names = ['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'Quoteassetvolume',
             'Numberoftrades', 'Takerbuybaseassetvolume', 'Takerbuyquoteassetvolume', 'Ignore']
    response = urllib.request.urlopen(url)

    df = pandas.read_json(response.read())

    # We will save this captured data to the computer.
    df.to_csv('BinanceData.csv', encoding='utf-8', index=False, header=False)

    # The recorded data will be graphed
    dataframe = pandas.read_csv('BinanceData.csv', names=names)

    # Calculations such as MACD SMA RSI will be made.
    stock = StockDataFrame.retype(dataframe)

    rsi12 = stock[InputLog_2]
    dataframe.opentime = pandas.to_datetime(dataframe.opentime, unit='ms')

    pyplot.subplot(211)
    pyplot.title(f'{Coin_Optioner} - {Currency_Optioner}')
    pyplot.plot(dataframe.opentime, dataframe.close)
    # The graph will be added to these calculations.
    pyplot.subplot(212)
    pyplot.title(f'{InputLog_2} - Indicator')
    pyplot.plot(dataframe.opentime, rsi12)
    pyplot.show()
