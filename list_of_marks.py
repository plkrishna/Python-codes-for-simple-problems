#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:18:57 2019

@author: plkrishna2211
"""
l=['a','b','c','d','e','f','g','h','i','j']
m1=[2,3,4,5,6,7,8,9,10,8]
m2=[1,5,6,7,4,3,6,3,1,8]
l_marks=[]
for i in range(0,10):
    l1=[l[i],m1[i],m2[i]]
    l_marks.append(l1)
for i in range(0,10):
    print(l_marks[i])
    