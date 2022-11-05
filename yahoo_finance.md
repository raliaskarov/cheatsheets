** Plot time series for EURUSD for past 1y daily close prices **
```
import yfinance as yf
ticker = yf.Ticker("EURUSD=X")
ticker_series = ticker.history(period = '1y',
              invetval = '1d').Close
x = ticker_series.index
y = ticker_series.values
plt.plot(x,y)
```
