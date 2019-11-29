#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:18:09 2019

@author: plkrishna2211
"""
s=""
stg=input('Enter a string:')
shifts=int(input('Number of shifts:'))
for i in stg:
    if ord(i) in range(97,123):
        if ord(i)+shifts>122:
            a=ord(i)+shifts-26
        else:
            a=ord(i)+shifts
        s=s+chr(a)
    elif ord(i) in range(65,91):
        if ord(i)+shifts>90:
            a=ord(i)+shifts-26
        else:
            a=ord(i)+shifts
        s=s+chr(a)
    else:
        s=s+i
print('Modified string:{}'.format(s))