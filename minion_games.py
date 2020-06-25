#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:06:02 2019

@author: plkrishna2211
"""
def m_game(s):
    vow=['A','E','I','O','U']
    k,s=0,0
    sub=(s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1))
    while True:
        try:
            ns=next(sub)
            if ns[0] in vow:
                k+=1
            else:
                s+=1
        except StopIteration:
            break
    if s>k:
        print('Stuart {}'.format(s))
    elif k>s:
        print('Kevin {}'.format(k))
    elif s==k:
        print('Draw')

def m_game1(s):
    
