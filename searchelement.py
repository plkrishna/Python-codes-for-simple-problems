#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:59:14 2019

@author: plkrishna2211
"""
def search(li,key):
    if len(li)==0:
        return 0
    if li[0]==key:
        return 1+search(li[1:],key)
    else:
        return search(li[1:],key)
