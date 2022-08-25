import backtrader as bt
import datetime
from strategy_buyhold import BuyHold

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
#add a strategy
engine.addstrategy(BuyHold)

#portfolio start value (before strategy is run) 
print(f'Portfolio value (start): {engine.broker.getvalue()}')

#run the engine
engine.run()
print(f"Portfolio value (end): {engine.broker.getvalue()}")

#plot results to a graph
engine.plot()