#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:38:59 2019

@author: plkrishna2211
"""
s1=input()
alphas=''
specials=''
nums=''
for i in s1:
    if i.isalpha():
        alphas=alphas+i
    elif i.isnumeric():
        nums=nums+i
    elif i !=' ':
        specials=specials+i
print(alphas,nums,specials,sep='\n')