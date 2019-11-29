#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:36:37 2019

@author: plkrishna2211
"""
caps=0
lows=0
line=input('Enter a string:')
for i in line:
    if i.isupper():
        caps=caps+1
    elif i.islower():
        lows=lows+1
    else:
        pass
print('Capitals:{},Smalls:{}'.format(caps,lows))
