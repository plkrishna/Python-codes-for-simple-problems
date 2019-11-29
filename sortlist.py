#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:08:42 2019

@author: plkrishna2211
"""
li=[['a',1],['b',4],['c',2],['d',4],['e',2],['f',1]]
def my(l):
    return l[1]
li.sort(key=my)
#print(li.index(['a',1]))
print(li)
