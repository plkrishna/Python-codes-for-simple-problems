#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:19:36 2019

@author: plkrishna2211
"""
s1=input()
s2=input()
news=''
uniqs1=''
uniqs2=''
for i in s1:
    if i in s2 and i not in news and i!=' ':
        news=news+i
    if i not in s2 and i not in uniqs1 and i!=' ':
        uniqs1=uniqs1+i
for i in s2:
    if i not in s1 and i not in uniqs2 and i!=' ':
        uniqs2=uniqs2+i
print('Common:',news)
print('Only in s1:',uniqs1)
print('Omly in s2:',uniqs2)