import backtrader as bt
import math

class BuyHold(bt.Strategy):
    def __init__(self):
        self.order = None
    
    def next(self):
        if self.order == None:
            size = math.floor(self.broker.cash/self.data.close)
            self.order = self.buy(size=size)
            print(f"BUY: {size} shares of SPY @ {self.data.close} ({self.datas[0].datetime.date(0)}) ")
        


