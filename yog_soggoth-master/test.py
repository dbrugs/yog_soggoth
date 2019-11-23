# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:43:51 2019

@author: brugs_bunny
"""
from get_your_data import write_path
import pandas as pd
from pandas import DataFrame


portfolio = DataFrame(pd.read_csv(write_path+('portfolio.csv')))

#portfolio['30 Day Vol'] = portfolio['Adj Close'].groupby(portfolio['Symbol'])
VXX= DataFrame(portfolio.loc[portfolio['Symbol'] == 'VXX'])
VTI= DataFrame(portfolio.loc[portfolio['Symbol'] == 'VTI'])
GLD= DataFrame(portfolio.loc[portfolio['Symbol'] == 'GLD'])
TLT = DataFrame(portfolio.loc[portfolio['Symbol'] == 'TLT'])
list = [VXX,VTI,GLD,TLT]

for i in list:
    i['30 Day Vol'] = i['Adj Close'].rolling(30).std()
    i['100 Day Vol'] = i['Adj Close'].rolling(30).std()
    i['1 Year Vol'] = i['Adj Close'].rolling(253).std()
    i['3 Year Vol'] = i['Adj Close'].rolling(253*3).std()


print(portfolio.groupby('Symbol').describe()['Daily Net Change'])
print(portfolio[['Symbol','Daily Net Change']].groupby(['Symbol']).sum())
