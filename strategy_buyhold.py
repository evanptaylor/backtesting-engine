import backtrader as bt
import math

class BuyHold(bt.Strategy):
    params = (
        ('ticker', 'SPY'),
        ('order_percentage', 1)
    )

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.order = None
    
    def next(self):
        if self.order == None:
            pos_size = (self.params.order_percentage * self.broker.cash)
            size = math.floor(pos_size/self.data.close)
            self.order = self.buy(size=size)
            self.log(f"BUY: {size} shares of SPY @ {self.data.close[0]}")


