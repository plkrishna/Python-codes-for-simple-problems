#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:25:33 2019

@author: plkrishna2211
"""
def length(s):
    if s=='':
        return 0
    else:
        return 1+length(s[1:])
