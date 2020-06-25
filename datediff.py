#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:11:50 2019

@author: plkrishna2211
"""
ou=''
cnt=0
from datetime import date
f=open(r'input.txt')
k=f.readline()
dates=k.split()
try:
    sday=int(dates[0][0:2])
    smon=int(dates[0][3:5])
    syear=int(dates[0][6:10])
    aday=int(dates[1][0:2])
    amon=int(dates[1][3:5])
    ayear=int(dates[1][6:10])
except (ValueError,IndexError):
  f1=open('output.txt','w')
  f1.write('error')
  f1.close()
d1=date(syear,smon,sday)
d2=date(ayear,amon,aday)
de=date(2019,12,30)
print(d1,d2)
if d2<d1:
  ou='Invalid'
elif d1<de or d2<de:
  ou='Invalid'
else:
  nds=(d2-d1).days
  wd1=d1.weekday()
  if wd1<5:
    cnt+=1
  cnt+=(nds//7)*5
  gar=nds%7
  for i in range(1,gar+1):
    if (wd1+i)%7 not in (5,6):
      cnt+=1
  ou=str(cnt)
f1=open('output.txt','w')
f1.write(ou)
f1.close()

