import backtrader as bt
import math
#set slow and fast moving average values(days)
SLOW_MA = 200
FAST_MA = 50

class MA_Crossover(bt.Strategy):
    #change params to edit percentage of portfolio used and the stock ticker
    params = (
        ("fast", FAST_MA),
        ("slow", SLOW_MA), 
        ("order_percentage", 1),
        ("ticker", "SPY")
    )
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f"{dt.isoformat()} => {txt}")

    def __init__(self):
        self.fast_MA = bt.indicators.SMA(
            self.data.close,
            period=self.params.fast,
            plotname=f'{FAST_MA} day MA'
        )
        self.slow_MA = bt.indicators.SMA(
            self.data.close,
            period=self.params.slow,
            plotname=f'{SLOW_MA} day MA'
        )
        self.crossover = bt.indicators.CrossOver(self.fast_MA, self.slow_MA)
    
    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                pos_size = (self.params.order_percentage*self.broker.cash)
                self.size = math.floor(pos_size/self.data.close)
                self.log(f"BUY: {self.size} shares of {self.params.ticker} @ {self.data.close[0]}")
                self.buy(size=self.size)
        
        if self.position.size>0:
            if self.crossover<0:
                self.log(f"SELL: {self.size} shares of {self.params.ticker} @ {self.data.close[0]}")
                self.close()