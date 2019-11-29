#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:54:44 2019

@author: plkrishna2211
"""
def fib_rec(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)

def fib_iter(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        f1=0
        f2=1
        for i in range(3,n):
            f3=f1+f2
            f1=f2
            f2=f3
        return f3

if __name__=='__main__':
    n=int(input())
    import timeit
    start=timeit.default_timer()
    fib_iter(n)
    end=timeit.default_timer()
    print(end-start)
