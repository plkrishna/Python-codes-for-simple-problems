#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:04:10 2020

@author: plkrishna2211
"""

def check(jump_time,K):
    n=len(jump_time)
    if n==1:
        return jump_time[0]*K
    elif n==2:
        return lcm(jump_time[0],jump_time[1])*K
    else:
        l1=lcm(jump_time[0],jump_time[1])
        for i in range(2,n):
            if l1%jump_time[i]==0:
                pass
            else:
                l1=lcm(l1,jump_time[i])
        return (l1*K)%1000000007
    

    
def lcm(a,b):
    return (a*b)//gcd(a,b)

def gcd(a,b):
    if a>b:
        while b:
            a,b=b,a%b
        return a 
    else:
        while a:
            a,b=b%a,a
        return b
    
if __name__=='__main__':
    n=int(input())
    k=int(input())
    l=list(map(int,input().split()))
    val=check(l,k)
    print(val)
    
    