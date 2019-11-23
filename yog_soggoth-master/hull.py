from get_your_data import spx,oil,oil_weekly,spx_weekly
from functions import linear_weight_moving_average
import numpy as np

dataset = [spx,spx_weekly,oil,oil_weekly]
'''
for df in dataset:
#hull moving average
    period = 13
    period2 = int(period/2)
    period3 = int(np.sqrt(period))
    close = df['Settle'].to_numpy()
    df['WMA'] = linear_weight_moving_average(close,period = period)
    df['WMA2'] = linear_weight_moving_average(close,period = period2)
    df['WMA_2X2'] = df['WMA2']*2
    df['WMA3'] = df['WMA_2X2'] - df['WMA']
    WMA3 = df['WMA3'].to_numpy()
    df['hull_moving_avg'] = linear_weight_moving_average(WMA3,period3)
    df.set_index(df['Date'], inplace=True)
    df['hull_moving_avg']        
    '''

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
