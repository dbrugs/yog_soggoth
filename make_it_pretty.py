import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import get_your_data as get
import matplotlib.dates as mdates

#Tableau colors
##############################################################################3
#https://tableaufriction.blogspot.com/2012/11/finally-you-can-use-tableau-data-colors.html
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

colorblind_10 = [(0,107,164),(255,128,14),(171,171,171),(89,89,89),(95,158,209),
                 (200,82,0),(137,137,137),(162,200,236),(255,188,121),(207,207,207)]

gray5 = [(96,99,106),(165,172,175),(65,68,81),(143,135,130),(207,207,207)]
colors = [tableau20,colorblind_10,gray5]
##########################################################################3
#matplotlib requires 0-1 scale
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)
for i in range(len(colorblind_10)):
    r, g, b = colorblind_10[i]
    colorblind_10[i] = (r / 255., g / 255., b / 255.)
for i in range(len(gray5)):
    r, g, b = gray5[i]
    gray5[i] = (r / 255., g / 255., b / 255.)

df = get.oil
df = df[['Date','Open','High','Low','Settle']]
oil = get.oil
hull = get.oil_weekly[['Date','Settle','hull_moving_avg']]
print(df.head(40))

fig = plt.figure()
fig.suptitle('OIL Price and regression Data')
ax = fig.add_subplot(2,1,1)
ax.set_title('Crude Oil Price', color = tableau20[9])
ax.set_facecolor(colorblind_10[6])
ax.figure.set_facecolor(gray5[2])
ax.tick_params(axis = 'x', colors = gray5[1])
ax.tick_params(axis = 'y', colors = gray5[1])
candlestick_ohlc(ax, df.values, width= 2, colorup=tableau20[4], colordown=tableau20[6])
ax.plot(hull['hull_moving_avg'])
ax.xaxis_date()

ax2 = fig.add_subplot(2,2,3)
ax3 = fig.add_subplot(2,2,4)

plt.show()

'''

oil = get.oil
##Oil
df = oil[['Date','Open','High','Low','Settle']]
fig = plt.figure()
fig.suptitle('Crude Oil Data and Volatility')
ax1 = fig.add_subplot(2,1,1)
ax1.set_title('OIL DAILY PRICE')
ax1.set_axisbelow(True)
ax1.tick_params(axis = 'x', colors = gray5[1])
ax1.set_facecolor(colorblind_10[6])
ax1.figure.set_facecolor(gray5[2])

candlestick_ohlc(ax1, df.values, width= 5, colorup=tableau20[4], colordown=tableau20[6])
ax2 = fig.add_subplot(2,2,3)
ax2.set_title('30 Day Vol z-score')
ax2.plot(oil['30 Day Vol z-score'])
ax3 = fig.add_subplot(2,2,4)
ax3.set_title('100 Day Vol z-score')
plt.show()

'''