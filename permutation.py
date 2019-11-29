#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:44:30 2019

@author: plkrishna2211
"""
s='ABC'
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i not in (k,j):
                print(s[i],s[j],s[k],sep='')
