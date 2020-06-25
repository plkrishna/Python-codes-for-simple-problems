#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:11:10 2019

@author: plkrishna2211
"""
l=int(input())
num_li=list(map(int,input().split()))
series=[num_li[0]]
cnt=0
for i in range(1,l):
    #print(series[len(series)-1])
    if num_li[i]<series[len(series)-1]:
        cnt+=len(series)*(len(series)+1)//2
        #print(series)
        series.clear()
    series.append(num_li[i])
    if i==l-1:
        cnt+=len(series)*(len(series)+1)//2
print(cnt)
