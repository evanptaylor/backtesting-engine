# backtesing-engine
### backtest buy/sell indicators and strategies on historical data
backtesting-engine is a market backtester using the Backtrader library. works with all stocks and commodities, as long as the price and volumn data is in .csv format.

below we can see how it works.
here's a simple strategy that looks uses a momentum indicator called the stochastic oscillator to buy/sell the s&p500 index:

#####first what it looks like in the command line:
![Screen Shot 2022-12-27 at 8 44 05 PM](https://user-images.githubusercontent.com/36122439/209744344-d5dd17b9-2f90-4672-96d0-9524fc95c1d5.png)
#####and then what we output using Backtrader/matplotlib
![Screen Shot 2022-12-27 at 8 44 19 PM](https://user-images.githubusercontent.com/36122439/209744337-7d95adb9-1633-429f-998a-294c7e526f34.png)
#####then we can compare that to just buying and holding the s&p:
![Screen Shot 2022-12-27 at 8 45 07 PM](https://user-images.githubusercontent.com/36122439/209744323-156a4528-3e5f-4052-a941-7626b2ab7f08.png)


