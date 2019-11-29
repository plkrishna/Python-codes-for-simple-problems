#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:27:41 2019

@author: plkrishna2211
"""
sen=input()
dec=0
for i in sen:
    if i.isdigit():
        dec=dec*2+int(i)
for i in sen:
    if not i.isdigit():
        print(i,end='')
    else:
        print(dec)
        break

