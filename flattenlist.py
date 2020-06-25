#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:05:24 2019

@author: plkrishna2211
"""
def flatten(li):
    if len(li)==0:
        return li
    if isinstance(li[0],list):
        return flatten(li[0])+flatten(li[1:])
    else:
        return [li[0]]+flatten(li[1:])
