#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:31:13 2019

@author: plkrishna2211
"""
a=len
def maxi(li):
    global a
    le=a(li)
    if le==1:
        return li[0]
    elif le==2:
        if li[0]>li[1]:
            return li[0]
        else:
            return li[1]
    else:
        max1=maxi(li[:le//2])
        max2=maxi(li[le//2:])
        if max1>max2:
            return max1
        else:
            return max2

def maxi_iter(li):
    maxi=li[0]
    for k in li[1:]:
        if k>maxi:
            maxi=k
    return maxi
