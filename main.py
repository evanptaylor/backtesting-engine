import backtrader as bt
import datetime
from strategy_buyhold import BuyHold
from strategy_moving_avg_cross import MA_Crossover
from strategy_stochastic_osc import Stochastic

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
#engine.addstrategy(BuyHold)
##engine.addstrategy(MA_Crossover)
engine.addstrategy(Stochastic)
#portfolio start value (before strategy is run) 
print(f'Portfolio value (start): {engine.broker.getvalue()}')

#run the engine
engine.run()
print(f"Portfolio value (end): {engine.broker.getvalue()}")

#plot results to a graph
engine.plot()