import numpy as np
import pandas as pd

def linear_weight_moving_average(signal, period):
    buffer = [np.nan] * period
    for i in range(period, len(signal)):
        buffer.append(
            (signal[i - period : i] * (np.arange(period) + 1)).sum()
            / (np.arange(period) + 1).sum()
        )
    return pd.Series(buffer)

def hull_moving_average(Dataset, period):
    period2 = int(period/2)
    period3 = int(np.sqrt(period))
    close = Dataset['Settle'].to_numpy()
    Dataset['WMA'] = linear_weight_moving_average(close,period = period)
    Dataset['WMA2'] = linear_weight_moving_average(close,period = period2)
    Dataset['WMA_2X2'] = Dataset['WMA2']*2
    Dataset['WMA3'] = Dataset['WMA_2X2'] - Dataset['WMA']
    WMA3 = Dataset['WMA3'].to_numpy()
    Dataset['hull_moving_avg'] = linear_weight_moving_average(WMA3,period3)
    Dataset.set_index(Dataset['Date'], inplace=True)
    return Dataset['hull_moving_avg']