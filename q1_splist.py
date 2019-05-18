# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:34:22 2019

@author: Kaushik
"""

import pandas as pd

global tickers

data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = data[0]
#print(table.head())
sliced_table = table[1:]
header = table.iloc[0]
corrected_table = sliced_table.rename(columns=header)
#print(corrected_table)
tickers = corrected_table['Symbol'].tolist()
#print (tickers)