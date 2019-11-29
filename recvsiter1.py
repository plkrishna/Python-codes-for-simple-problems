#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:34:33 2019

@author: plkrishna2211
"""
def fact_iter(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac


def fact_rec(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact_rec(n-1)


if __name__=='__main__':
    n=int(input())
    import timeit
    start=timeit.default_timer()
    fact_rec(n)
    end=timeit.default_timer()
    print(end-start)
