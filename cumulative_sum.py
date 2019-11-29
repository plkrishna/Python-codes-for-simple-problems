#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:57:20 2019

@author: plkrishna2211
"""
l1=[]
while True:
    a=input()
    if a=='stop':
        break
    l1.append(int(a))
l2=[]
summ=0
for i in range(len(l1)):
    summ=summ+l1[i]
    l2.append(summ)
print('Cumulative sums:',l2,sep='\n')