#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 06:04:26 2020

@author: plkrishna2211
"""

def process(brs,n,d,x):
    maxes=[find(i,d) for i in brs]
    #high=max(maxes)
    #print(maxes)
    for i in range(n-2,-1,-1):
        if maxes[i]<=maxes[i+1]:
            pass
        else:
            while maxes[i]>maxes[i+1]:
                maxes[i]-=brs[i]
    print('Case #{}: {}'.format(x,maxes[0]))
        
        
    
def find(h,d):
    return h*(d//h)
if __name__=='__main__':
    t=int(input())
    ns=[]
    ds=[]
    ips=[]
    for i in range(t):
        n,d=tuple(map(int,input().split()))
        ns.append(n)
        ds.append(d)
        ips.append(list(map(int,input().split())))
    for i in range(t):
        process(ips[i],ns[i],ds[i],i+1)