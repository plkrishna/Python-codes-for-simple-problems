#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:01:46 2019

@author: plkrishna2211
"""
d={0:0}
def tdcoins(val,li):
    if d.get(val,-1)==-1:
        d[val]=min([1+tdcoins(val-i,li) for i in li if i<=val])
        return d[val]
    else:
        return d[val]

import sys as s
def rcoins(val,li):
    if val==0:
        return 0
    else:
        r=s.maxsize
        for x in li:
            if x<=val:
                r=min(r,1+rcoins(val-x,li))
        return r
bt={0:0}
def btcoins(v,l):
    for i in range(1,v+1):
        bt[i]=s.maxsize
    for value in range(1,v+1):
        for x in l:
            if x<=value:
                si=bt[value-x]
                if si+1<bt[value]:
                    bt[value]=si+1
    return bt[v]
    

import timeit as t

if __name__=='__main__':
    l=eval(input())
    v=int(input())
    st=t.default_timer()
    print(btcoins(v,l))
    en=t.default_timer()
    print(en-st)
    