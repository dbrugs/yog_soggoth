import pandas as pd
from pandas import DataFrame
import matplotlib.dates as mdates
import numpy as np
from functions import linear_weight_moving_average

write_path = r'/home/brugs_bunny/scripts/script_data//'

oil = DataFrame(pd.read_csv(write_path+'oil.csv',))
oil_weekly = DataFrame(pd.read_csv(write_path+'oil_weekly.csv',))
oil_monthly = DataFrame(pd.read_csv(write_path+'oil_monthly.csv',))
oil_list = [oil,oil_weekly,oil_monthly]

gold = DataFrame(pd.read_csv(write_path+'gold.csv'))
gold_weekly = DataFrame(pd.read_csv(write_path+'gold_weekly.csv'))
gold_monthly = DataFrame(pd.read_csv(write_path+'gold_monthly.csv'))
gold_list = [gold,gold_weekly, gold_monthly]

spx = DataFrame(pd.read_csv(write_path+'sp500.csv'))
spx_weekly = DataFrame(pd.read_csv(write_path + 'es_weekly.csv'))
spx_monthly = DataFrame(pd.read_csv(write_path + 'es_monthly.csv'))
spx_list = [spx,spx_weekly,spx_monthly]

ndx = DataFrame(pd.read_csv(write_path+'nasdaq.csv'))
ndx_weekly = DataFrame(pd.read_csv(write_path + 'nsdq_weekly.csv'))
ndx_monthly = DataFrame(pd.read_csv(write_path + 'nsdq_monthly.csv'))
ndx_list = [ndx,ndx_weekly,ndx_monthly]

dollar = DataFrame(pd.read_csv(write_path+'USD.csv'))
dollar_weekly = DataFrame(pd.read_csv(write_path + 'dollar_weekly.csv'))
dollar_monthly = DataFrame(pd.read_csv(write_path + 'dollar_monthly.csv'))
dollar_list = [dollar,dollar_weekly,dollar_monthly]

two_year = DataFrame(pd.read_csv(write_path+'2YR.csv'))

ten_year = DataFrame(pd.read_csv(write_path+'10YR.csv'))
interest_rates = [two_year,ten_year]


#get the VOL data
vix = DataFrame(pd.read_csv(write_path+'vix.csv'))
vx1 = DataFrame(pd.read_csv(write_path+'vx1.csv'))
vx2 = DataFrame(pd.read_csv(write_path+'vx2.csv'))
vx3 = DataFrame(pd.read_csv(write_path+'vx3.csv'))
vx4 = DataFrame(pd.read_csv(write_path+'vx4.csv'))
vx5 = DataFrame(pd.read_csv(write_path+'vx5.csv'))
vix_curve = [vx1,vx2,vx3,vx4, vx5]

for df in vix_curve:
    df.rename(columns = {'Trade Date': 'Date'}, inplace = True)
vix_curve.append(vix)

asset_dict = {'oil':oil_list,'gold': gold_list,'spx': spx_list,
'ndx': ndx_list, 'dollar':dollar_list, 'interest_rates': interest_rates,
'vol':vix_curve}

assets = [oil,gold,spx,ndx,dollar,two_year, oil_monthly, oil_weekly,]

for df in assets:    
    df['Date'] = df['Date'].map(mdates.datestr2num)
for df in vix_curve:
   df['Date'] = df['Date'].map(mdates.datestr2num)


weekly_list = [oil_weekly,gold_weekly,spx_weekly,ndx_weekly]
monthly_list = [oil_monthly,gold_monthly,spx_monthly,ndx_monthly]
master_list = weekly_list+monthly_list
##Weekly return data
for df in master_list:
    df['Previous Settle'] = df['Settle'].shift(1)
    df['Net Change'] = df['Settle'] - df['Previous Settle']
    df['Absolute Change'] = df['Net Change'].abs()
    df['Returns'] = (np.log(df['Settle'] / df['Previous Settle']))
   
   
'''This is the end of the actual code, the bottom is beta'''    
   
   
   
   
   ###############################################################################
    ############################################################
##########################################################    
period = 13
period2 = int(period/2)
period3 = int(np.sqrt(period))
close = oil['Settle'].to_numpy()
oil['WMA'] = linear_weight_moving_average(close,period = period)
oil['WMA2'] = linear_weight_moving_average(close,period = period2)
oil['WMA_2X2'] = oil['WMA2']*2
oil['WMA3'] = oil['WMA_2X2'] - oil['WMA']
WMA3 = oil['WMA3'].to_numpy()
oil['hull_moving_avg'] = linear_weight_moving_average(WMA3,period3)
oil.set_index(oil['Date'], inplace=True)

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

