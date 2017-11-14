#! /usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
from pandas import DataFrame

import time,sched,os

def getpage():
    r=requests.get('http://www.touhou.ren/GP.aspx')
    rt=r.text
    soup=BeautifulSoup(rt,'lxml')
    #print(soup.prettify())

    l=[]
    for string in soup.stripped_strings:
        l.append(string)
    return l

def getdata(n=36):
    x=14
    y=36*9+x
    l_main=getpage()[x:y]
    data_array=np.array(l_main)
    l_col=['number','name','price_now','price_init','range','buy','sell','after_tax','introduction']
    data_new=DataFrame(data_array.reshape(n,9),index=range(1,n+1),columns=l_col)
    del data_new['name']
    del data_new['introduction']
    data_new['time']=getpage()[4]
    data_new['number']='n'+data_new['number']

    if os.path.exists(r'touhougp.csv'):
        data_old=pd.read_csv('touhougp.csv',encoding='utf-8')
        if data_old.iat[-1,-1]!= data_new.iat[-1,-1]:
            data=pd.concat([data_old,data_new],ignore_index=True)
            data.to_csv('touhougp.csv',index=False,encoding='utf-8')
        else:
            data=data_old
    else:
        data=data_new
        data.to_csv('touhougp.csv',index=False,encoding='utf-8')
    return data
print(getdata())
