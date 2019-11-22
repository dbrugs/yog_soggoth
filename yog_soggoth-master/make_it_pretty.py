import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import get_your_data as get
from settings import tableau20, gray5
#from hull import dataset

df = get.oil
#df_weekly = get.oil_weekly[['Date','Settle','hull_moving_avg']] 
df = df[['Date','Open','High','Low','Settle',]]

oil = get.oil
oil.set_index(oil['Date'], inplace = True)
hull = get.oil_weekly[['Date','Settle','hull_moving_avg']]
hull.set_index(hull['Date'],inplace = True)
fig = plt.figure()
fig.suptitle('OIL Price and Vol Data')

##AX 1 Price and Tech Data
ax = fig.add_subplot(2,1,1)
ax.set_title('Crude Oil Price', color = tableau20[8])
ax.set_facecolor(tableau20[15])
ax.grid(True)
ax.figure.set_facecolor(gray5[1])
ax.tick_params(axis = 'x', colors = gray5[2])
ax.tick_params(axis = 'y', colors = gray5[2])
candlestick_ohlc(ax, df.values, width= 2, colorup=tableau20[4], colordown=tableau20[6])
ax.plot(oil['SMA long'], color = tableau20[18])
ax.plot(hull['hull_moving_avg'],color = tableau20[8])
ax.legend()
ax.xaxis_date()

##AX 2 VOl DATA
ax2 = fig.add_subplot(2,1,2)
ax2.set_facecolor(tableau20[15])
ax2.tick_params(axis = 'x', colors = gray5[2])
ax2.tick_params(axis = 'y', colors = gray5[2])
ax2.grid(True)
ax2.plot(oil['30 Day Vol'], color = tableau20[8])
ax2.plot(oil['100 Day Vol'], color = tableau20[18])
ax2.legend()
#create print for stamps on Mean Vol and Vol.today()


ax2.xaxis_date()
#ax3 = fig.add_subplot(2,2,4)
#ax3.set_facecolor(colorblind_10[6])

plt.show()
