#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:38:20 2019

@author: plkrishna2211
"""
l=[1,2,1,2,3,4,3,5,1,2,4,6,5,1,3,9,10,2]
l1=[]
dup=[]
for i in l:
    if i in l1:
        dup.append(i)
    if i not in l1:
        l1.append(i)
print(l1)
print(dup)
