#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:09:51 2019

@author: plkrishna2211
"""
def irev_st(sam):
    k=len(sam)
    rev=''
    for i in range(k-1,-1):
        rev+=sam[i]
    return rev
a=len
def rrev_st(sam):
    global a
    if a(sam)==0:
        return sam
    else:
        return sam[-1]+rrev_st(sam[:a(sam)-1])
    


    
    
    