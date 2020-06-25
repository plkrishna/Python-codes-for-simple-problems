#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:46:01 2019

@author: plkrishna2211
"""

def mp(li,n):
    if n==0:
        return 0
    else:
        return max([li[i]+mp(li,n-i-1) for i in range(len(li)) if i+1<=n])



d={0:0}
def tdmp(li,n):
    if d.get(n,-1)==-1:
        d[n]=max([li[i]+tdmp(li,n-i-1) for i in range(len(li)) if i+1<=n])
        return d[n]
    else:
        return d[n]

bu={0:0}
def bump(li,n):
    for i in range(1,n+1):
        bu[i]=-999
    for k in range(1,n+1):
        for i in range(len(l)):
            if i+1<=k:
                bu[k]=max(bu[k],li[i]+bu[k-i-1])
    return bu[n]

def greedymp(li,n):
    i=len(li)-1
    p=0
    while i>=0:
        if n==0:
            break
        elif i<=n:
            n=n-i-1
            p+=li[i]
        elif i>n:
            i-=1
    return p

if __name__=='__main__':
    import timeit as t
    l=eval(input())
    v=int(input())
    st=t.default_timer()
    print(greedymp(l,v))
    en=t.default_timer()
    print(en-st)
    