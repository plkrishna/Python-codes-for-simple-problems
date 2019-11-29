#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:22:50 2019
@author: plkrishna2211
"""
def binary(n):
    if n==1:
        return '1'
    elif n==0:
        return '0'
    else:
        return binary(n//2)+str(n%2)
