import backtrader as bt
import datetime
import argparse

from strategy_buyhold import BuyHold
from strategy_moving_avg_cross import MA_Crossover
from strategy_stochastic_osc import Stochastic

#map string vals from argparse to object names
strats = {
    "Stochastic": Stochastic,
    "BuyHold": BuyHold,
    "MA_Crossover": MA_Crossover
}
#add option for argparse from user
parser = argparse.ArgumentParser(description="backtestng-engine")
parser.add_argument("-d", "--data", required=True )
parser.add_argument("-s", "--strategy", required=True)
parser.add_argument("-v", "--value", required=True)
args = parser.parse_args()

#set parsed values to relevant vars
CSV_DATA = args.data
STRATEGY = strats[args.strategy]
PORTFOLIO_VALUE = float(args.value)

#instatiate cerebro engine
engine = bt.Cerebro()
#set portfolio value to $10,000
engine.broker.set_cash(PORTFOLIO_VALUE)

#import stock price from Yahoo Finance CSV
data = bt.feeds.YahooFinanceCSVData(
    dataname = CSV_DATA,
    reverse = False
)
#add data to engine
engine.adddata(data)
#add a strategy
engine.addstrategy(STRATEGY)
#portfolio start value (before strategy is run) 
print(f"Portfolio value (start): {engine.broker.getvalue()}")

#run the engine (iterate strategy over data)
engine.run()
print(f"Portfolio value (end): {engine.broker.getvalue()}")

#plot
engine.plot()