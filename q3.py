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


pathd =r'D:\Msit\DADV\visualization_exam\daily_data' # DAILY
pathm =r'D:\Msit\DADV\visualization_exam\monthly_data' # MONTHLY
pathw =r'D:\Msit\DADV\visualization_exam\weekly_data' # WEEKLY

def sort_dict(d):
    sorted_by_value = sorted(d.items(), key=lambda kv: kv[1])
    return sorted_by_value


def q3heatmap(path_d):
    dict_d={}
    dict_d_temp={}
    
    df_corr=pd.DataFrame()
    
    allFiles = glob.glob(path_d + "/*.csv")
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=0)
        max_gain = ((df.iloc[0]['Close'])-(df.iloc[len(df)-1]['Close']))/(df.iloc[len(df)-1]['Close'])
        s= (file_.split('\\')[-1])
        dict_d[s[:-4]] = max_gain
        df_corr[s[:-4]] = (df['Gain_or_Loss_%'])
      
    df_corr=df_corr.dropna()
    
    corr = df_corr.corr()
    
    
    cdict = {'blue':  ((0.0, 0.0, 0.0),   # no red at 0
                      (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                      (1.0, 0.8, 0.8)),  # set to 0.8 so its not too bright at 1
    
            'red': ((0.0, 0.8, 0.8),   # set to 0.8 so its not too bright at 0
                      (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                      (1.0, 0.0, 0.0)),  # no green at 1
    
            'green':  ((0.0, 0.0, 0.0),   # no blue at 0
                      (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                      (1.0, 0.0, 0.0))   # no blue at 1
           }
    
    GnRdBe = colors.LinearSegmentedColormap('GnRdBe', cdict)
    fig,ax = plt.subplots(1)
    data = corr
    p=ax.pcolormesh(data,cmap=GnRdBe,vmin=-1,vmax=1)
    fig.colorbar(p,ax=ax)
    fig.set_size_inches(10, 10)
    plt.show()
    
q4heatmap(pathd)
q4heatmap(pathm)
q4heatmap(pathw)