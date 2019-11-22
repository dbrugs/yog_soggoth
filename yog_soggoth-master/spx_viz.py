import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import get_your_data as get
from settings import tableau20


df = get.spx
df_weekly = get.spx_weekly[['Date','Settle']]
df_weekly.set_index(df_weekly['Date'], inplace = True) 
df = df[['Date','Open','High','Low','Settle',]]

spx = get.spx
spx.set_index(spx['Date'], inplace = True)

fig = plt.figure()
fig.suptitle('SPX PRICE AND VOL DATA')

ax1 = fig.add_subplot(2,1,1)
candlestick_ohlc(ax1, df.values, width= 2, colorup=tableau20[4], colordown=tableau20[6])
ax1.plot(spx['SMA long'])
ax1.xaxis_date()

ax2 = fig.add_subplot(2,1,2)
df = get.vix
df.set_index(df['Date'], inplace = True)
ax2.plot(df['Adj Close'])
df = get.vx1
df.set_index(df['Date'], inplace = True)
ax2.plot(df['Settle'])
ax2.xaxis_date()

plt.show()
