#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:19:31 2019

@author: plkrishna2211
"""
l1=[1,2,3,4,5]
for i in range(1,len(l1)):
    l1[i]=l1[i]+l1[i-1]
print(l1)