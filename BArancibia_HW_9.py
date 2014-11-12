#Benjamin Arancibia
#11/11/2014
#Week 9 Assignment

import os
import csv
import Tkinter
import tkFileDialog
import pandas as pd
import numpy as np

epa_http = pd.read_csv('/users/bcarancibia/CUNY_IS_602/Lesson9/epa_http_http.txt', 
                  delim_whitespace = True, 
                  error_bad_lines = False,
                  names = ['host', 'date', 'request', 'reply-code', 'bytes'],
                  header = None)



for i in range(len(epa_http['bytes'])):
    if not epa_http['bytes'][i].isdigit():
       epa_http['bytes'][i] = 0
       
epa_http['bytes'] = epa_http['bytes'].astype(int)

for i in range(len(epa_http)):
   epa_http['date'][i] = epa_http['date'][i][1:-1]
   tmp = epa_http['date'][i].split(':')
   epa_http['date'][i] = "Day: " + tmp[0] + " Hour: " + tmp[1]


epa_http = epa_http[epa_http['reply-code'] != 'HTTP/1.0"']


##### 1 #####
hostrequestsmost = epa_http['host'].value_counts().index[0]


##### 2 #####
sortedbytes = epa_http.groupby('host').sum().sort('bytes', ascending=False)['bytes']

##### 3 #####

busiestHour = epa_http['date'].value_counts().index[0]

##### 4 #####
# get /image.gif HTTP/1.0
gifs = epa_http[epa_http['request'].str.contains('gif')]
gifsMost = gifs['request'].value_counts().index[0]

##### 5 #####
replies = epa_http['reply-code'].unique()
repNotTwoHundo = replies[replies != '200']

##### Output #####
# 1
print '*' *25
print '#1'
print 'Most requests made by: '
print hostrequestsmost
print '*' *25
# 2
print '#2'
print 'Most received bytes by: '
print sortedbytes.index[0]
print 'Received bytes: '
print sortedbytes[0]
print '*' *25
# 3
print '#3'
print 'Busiest hour: '
print busiestHour
print '*' *25
# 4
print '#4'
print 'Most downloaded gif: '
print gifsMost
print '*' *25
# 5
print '#5'
print 'HTTP Reply codes other than 200: '
print repNotTwoHundo
print '*' *25