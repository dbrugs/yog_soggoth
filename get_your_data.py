import pandas as pd
from pandas import DataFrame
import matplotlib.dates as mdates
from functions import linear_weight_moving_average
import numpy as np

write_path = r'C:\Users\Faye Brugman\Desktop\pythonscripts\viper_data\\'
oil = DataFrame(pd.read_csv(write_path+'oil.csv',))
oil_weekly = DataFrame(pd.read_csv(write_path+'oil_weekly.csv',))
oil_monthly = DataFrame(pd.read_csv(write_path+'oil_monthly.csv',))

gold = DataFrame(pd.read_csv(write_path+'gold.csv'))
gold_weekly = DataFrame(pd.read_csv(write_path+'gold_weekly.csv'))

spx = DataFrame(pd.read_csv(write_path+'sp500.csv'))
spx_weekly = DataFrame(pd.read_csv(write_path + 'es_weekly.csv'))
spx_monthly = DataFrame(pd.read_csv(write_path + 'es_monthly.csv'))

ndx = DataFrame(pd.read_csv(write_path+'nasdaq.csv'))

dollar = DataFrame(pd.read_csv(write_path+'USD.csv'))

two_year = DataFrame(pd.read_csv(write_path+'2YR.csv'))

assets = [oil,gold,spx,ndx,dollar,two_year, oil_monthly, oil_weekly]
for df in assets:
    df['Date'] = df['Date'].map(mdates.datestr2num)

#get the VOL data
vix = DataFrame(pd.read_csv(write_path+'vix.csv'))
vx1 = DataFrame(pd.read_csv(write_path+'vx1.csv'))
vx2 = DataFrame(pd.read_csv(write_path+'vx2.csv'))
vx3 = DataFrame(pd.read_csv(write_path+'vx3.csv'))
vx4 = DataFrame(pd.read_csv(write_path+'vx4.csv'))
vx5 = DataFrame(pd.read_csv(write_path+'vx5.csv'))

vix_curve = [vix, vx1,vx2,vx3,vx4, vx5]
#for df in vix_curve:
 #   df['Date'] = df['Date'].map(mdates.datestr2num)

##Weekly return data
oil_weekly['Previous Settle'] = oil_weekly['Settle'].shift(1)
oil_weekly['Net Change'] = oil_weekly['Settle'] - oil_weekly['Previous Settle']
oil_weekly['Absolute Change'] = oil_weekly['Net Change'].abs()
oil_weekly['Returns'] = (np.log(oil_weekly['Settle'] / oil_weekly['Previous Settle']))

#hull moving average
period = 13
period2 = int(period/2)
period3 = int(np.sqrt(period))
close = oil_weekly['Settle'].to_numpy()
oil_weekly['WMA'] = linear_weight_moving_average(close,period = period)
oil_weekly['WMA2'] = linear_weight_moving_average(close,period = period2)
oil_weekly['WMA_2X2'] = oil_weekly['WMA2']*2
oil_weekly['WMA3'] = oil_weekly['WMA_2X2'] - oil_weekly['WMA']
WMA3 = oil_weekly['WMA3'].to_numpy()
oil_weekly['hull_moving_avg'] = linear_weight_moving_average(WMA3,period3)
oil_weekly.set_index(oil_weekly['Date'], inplace=True)
