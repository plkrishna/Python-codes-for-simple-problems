#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:34:31 2019

@author: plkrishna2211
"""
def sumeve(n):
    if n==0:
        return 0
    elif (n)%2!=0:
        return sumeve(n-1)
    else:
        return n+sumeve(n-2)

def sumodd(n):
    if n==1:
        return 1
    elif n%2==0:
        return sumodd(n-1)
    else:
        return n+sumodd(n-2)
    
def feve(n):
    if n==0:
        return 0
    else:
        return feve(n-1)+n*2

def fodd(n):
    if n==0:
        return 0
    else:
        return fodd(n-1)+(n*2-1)