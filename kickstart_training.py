#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:48:06 2019

@author: plkrishna2211
"""
import sys as s
def check(li,n,p):
    li.sort()
    charge=s.maxsize
    low=0
    high=p
    charge1=li[high-1]*(p-1)-sum(li[low:high-1])
    while high<=n:
        if charge1<charge:
            charge=charge1
        charge1=charge1-(li[high-1]*(p-1))+li[low]
        high+=1
        low+=1
        if high<=n:
            charge1=charge1+(li[high-1]*(p-1))-li[high-2]
    return charge
if __name__=='__main__':
    t=int(input())
    ips=[]
    ranges=[]
    for i in range(t):
        k=tuple(map(int,input().split()))
        ips.append(list(map(int,input().split())))
        ranges.append(k)
    for i in range(t):
        print('Case #{}: {}'.format(i+1,check(ips[i],ranges[i][0],ranges[i][1])))
    