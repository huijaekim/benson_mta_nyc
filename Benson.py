#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:36:48 2017

@author: chintan
"""
import csv
import pandas as pd
import requests
import urllib
import io
from datetime import datetime,timedelta

url = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_170916.txt'

date_f='170916'
df = datetime.strptime(date_f, '%y%m%d')


list_of_dates = []
list_of_dates.append(df)
for x in range(1,100):
    temp=df.today()-timedelta(days=7*x)
    list_of_dates.append(temp)


    print(str(list_of_dates[x].year)[2:])
    print(str(list_of_dates[x].month))
    print(str(list_of_dates[x].day))
    print('\n')
    


'''
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
'''