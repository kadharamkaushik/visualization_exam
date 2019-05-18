# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:35:38 2019

@author: Kaushik
"""

import glob
import pandas as pd

pathd =r'D:\Msit\DADV\visualization_exam\daily_data' # DAILY
pathm =r'D:\Msit\DADV\visualization_exam\monthly_data' # MONTHLY
pathw =r'D:\Msit\DADV\visualization_exam\weekly_data' # WEEKLY


def addgainloss(path):
    allFiles = glob.glob(path + "/*.csv")
    
    #df=pd.DataFrame()
    #df.columns=['Date','Open','High','	Low','Close*,''Adj Close**','Volume']
    
    list_=[]
    
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=0)
        s=(str)(file_)
    #    df['CompanyName']=s
    #    list_.append(df)
        df['Close']=pd.to_numeric(df['Close'])
        df['Gain_or_Loss_%'] = -(df[['Close']].pct_change()[1:])
        df.to_csv(file_)

addgainloss(pathd)
addgainloss(pathw)
#addgainloss(pathm)    