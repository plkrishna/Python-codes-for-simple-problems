#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:54:16 2019

@author: plkrishna2211
"""
lis=[]
pos=int(input('Position:'))
ele=int(input('Element:'))
if pos>0:
    for i in range(pos):
        lis.append(0)
    high=pos
else:
    high=0
lis.append(ele)
pos=int(input('Position:'))
ele=int(input('Element:'))
if pos>high:
    for i in range(high+1,pos):
        lis.append(0)
    lis.append(ele)
    high=pos
elif pos<high:
    lis.insert(pos,ele)
print(lis)

    

    