# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:38:30 2019

@author: Kaushik
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:17:39 2018

@author: Kaushik
"""
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

path_d =r'D:\Msit\DADV\visualization_exam\daily_data'

def sort_dict(d):
    sorted_by_value = sorted(d.items(), key=lambda kv: kv[1])
    return sorted_by_value

dict_d={}
dict_d_temp={}

allFiles = glob.glob(path_d + "/*.csv")
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=0)
    max_gain = ((df.iloc[0]['Close'])-(df.iloc[len(df)-1]['Close']))/(df.iloc[len(df)-1]['Close'])
    s= (file_.split('\\')[-1])
    dict_d[s[:-4]] = max_gain
    dict_d_temp[s[:-4]] = pd.Series(df['Gain_or_Loss_%'])
    

dict_d=sort_dict(dict_d)

corr_d=[]

for x in range(len(dict_d)):
    temp=[]
    for y in range(len(dict_d)):
        temp.append(np.corrcoef(dict_d_temp[dict_d[0][0]][1:],dict_d_temp[dict_d[0][0]][1:])[0][1])
#        print (dict_d_temp[dict_d[x][0]][1:])
#        print (dict_d_temp[dict_d[y][0]])
    corr_d.append(temp)

