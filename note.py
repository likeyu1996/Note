# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:03:56 2017

@author: dell
"""

'''x=input('被除数')
y=input('除数')
print (eval(x)/eval(y))'''
'''import math
print (dir(__builtin__))
print (dir(math))'''
import pandas as pd
import numpy as np
import matplotlib.pyplot  as  plt
import math
import seaborn as sns
from levy import*
import tushare as ts
h_sh=ts.get_hist_data('sh')

'''h_sh=pd.read_csv('F:\py\his of sh.csv')'''
price=h_sh['close']
lrate=price

for i in range(len(price)):
    if i<len(price)-1:
        lrate[i]=math.log(price[i])-math.log(price[i+1])
    else:
        lrate[i]=None
        
log_rate=lrate[:len(lrate)-1].to_frame(name='log rate')
slr=log_rate.sort_values(by='log rate')
sns.distplot(slr['log rate'],bins=70)
slr_mean=slr.mean()['log rate']
slr_std=slr.std()['log rate']
slr_l=list(slr['log rate'])
norm=np.random.normal(loc=slr_mean,scale=slr_std,size=100000)
sns.distplot(norm)
''