#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:53:23 2019

@author: plkrishna2211
"""
s='abcdefghijklmnopqrstuvwxyz'
#print(len(s))
s2=input()
n=int(input())
ns=''
for c in s2:
    if c.isalpha():
        i=s.index(c)
        ni=(i+n)%26
        ns=ns+s[ni]
    else:
        ns=ns+c
print(ns)

        
