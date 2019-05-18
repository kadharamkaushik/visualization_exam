# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:50:21 2018

@author: Kaushik
"""

import q1_splist as c
import numpy as np
import matplotlib.pyplot as plt
import collections
import glob
import pandas as pd

def sort_dict(d):
    sorted_by_value = sorted(d.items(), key=lambda kv: kv[1])
    return sorted_by_value

#print(c.table[3])
top4={}
bottom4={}
dict_d={}

path_d =r'D:\Msit\DADV\visualization_exam\daily_data' # DAILY
allFiles = glob.glob(path_d + "/*.csv")
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=0)
    max_gain = ((df.iloc[0]['Close'])-(df.iloc[len(df)-1]['Close']))/(df.iloc[len(df)-1]['Close'])
    s= (file_.split('\\')[-1])
    dict_d[s[:-4]] = max_gain
dict_d=sort_dict(dict_d)




temp_b=dict_d[0:25]
temp_t=dict_d[-25:]
sectors=[]

for val in temp_b:
#    print (val[0])
    temp= (c.table.loc[c.table[0] == val[0]])
    temp=(temp.iloc[0][3])
#    print (temp)
#    print ((type)(temp))
    if temp not in sectors:
            sectors.append(temp)
#    print ()
#    print ((type)(temp[3]))
#    print((type)(temp[3]))
#    print(s)
    
    if(temp in bottom4):
        bottom4[temp]+=1
    else:
        bottom4[temp]=1

for val in temp_t:
#    print (val[0])
    temp= (c.table.loc[c.table[0] == val[0]])
    temp=(temp.iloc[0][3])
    if temp not in sectors:
            sectors.append(temp)
    if(temp in top4):
        top4[temp]+=1
    else:
        top4[temp]=1
    


for x in sectors:
    if x not in top4:
        top4[x]=0
    if x not in bottom4:
        bottom4[x]=0

top4 = collections.OrderedDict(sorted(top4.items()))

bottom4 = collections.OrderedDict(sorted(bottom4.items()))

f, ax = plt.subplots(figsize=(18,5))
X = np.arange(len(top4))
ax = plt.subplot(111)
ax.bar(X, top4.values(), width=0.3, color='b', align='center')
ax.bar(X-0.3, bottom4.values(), width=0.3, color='r', align='center')
ax.legend(('top4','bottom4'))
plt.xticks(X, top4.keys())
plt.title("Accuracy score", fontsize=17)
plt.show()    
