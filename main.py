import backtrader as bt
import datetime

#instatiate cerebro engine
engine = bt.Cerebro()
#set portfolio value to $10,000
engine.broker.set_cash(10000)

#import stock price from Yahoo Finance CSV
data = bt.feeds.YahooFinanceCSVData(
    dataname = "SPY_5Year.csv",
    reverse = False
)
#add data to engine
engine.adddata(data)

