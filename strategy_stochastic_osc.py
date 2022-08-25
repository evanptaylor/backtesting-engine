import backtrader as bt
import math

class Stochastic(bt.Strategy):
    params = (
        ('order_percentage', 1),
        ('ticker', "SPY"),
        ('top_bound', 82.5),
        ('bottom_bound', 17.5)
    )
    
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f"{dt.isoformat()} => {txt}")

    def __init__(self):
        self.sto = bt.indicators.Stochastic(self.data)
        self.crossed_top = False
        self.crossed_bottom = False

    def next(self):
        current_k = self.sto.lines.percK[0]
        prev_k = self.sto.lines.percK[-1]

        if current_k > self.params.top_bound:
            self.crossed_top = True
        elif current_k < self.params.bottom_bound:
            self.crossed_bottom = True

        if self.position.size == 0:
            if prev_k < self.params.bottom_bound and current_k < self.params.bottom_bound:
                pos_size = (self.broker.getcash()*self.params.order_percentage)
                self.size = math.floor(pos_size/self.data.close)
                self.buy(size=self.size)
                self.log(f"BUY: {self.size} shares of {self.params.ticker} @ {self.data.close[0]}")

        if self.position.size > 0:
            if current_k < 50 and self.crossed_top:
                self.close()
                self.log(f"SELL: {self.size} shares of {self.params.ticker} @ {self.data.close[0]}")
                self.crossed_top = False
    