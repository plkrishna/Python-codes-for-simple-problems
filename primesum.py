#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:50:40 2019

@author: plkrishna2211
"""
su=0
import math as m
n=5
for x in range(2,n+1):
    prime=True
    for i in range(2,x//2+1):
        if x%i==0:
            prime=False
            break
    if prime:
        su+=x
print('Sum:',su);
