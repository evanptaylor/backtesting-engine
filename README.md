# backtesing-engine
### backtest buy/sell indicators and strategies on historical data
backtesting-engine is a market backtester using the Backtrader library. works with all stocks and commodities, with price and volumn data in .csv format.

below we can see how it works.
here's a simple strategy that uses a momentum indicator called the stochastic oscillator to buy/sell the s&p500 index:

##### our view in the command line:
![Screen Shot 2022-12-27 at 8 44 05 PM](https://user-images.githubusercontent.com/36122439/209744344-d5dd17b9-2f90-4672-96d0-9524fc95c1d5.png)
##### our strategy visualized with matplotlib
![Screen Shot 2022-12-27 at 8 44 19 PM](https://user-images.githubusercontent.com/36122439/209744337-7d95adb9-1633-429f-998a-294c7e526f34.png)
##### then we test the strategy's effectivness by comparing it to the performance of simply buying and holding the s&p over the same time period:
![Screen Shot 2022-12-27 at 8 45 07 PM](https://user-images.githubusercontent.com/36122439/209744323-156a4528-3e5f-4052-a941-7626b2ab7f08.png)
As we can see, buying a holding actually outpreforms this specific strategy. It is pretty tough to outperform this run of the s&p 500.

