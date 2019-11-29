#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:15:10 2019

@author: plkrishna2211
"""
def outer(name):
    def inner(sym):
        return name.center(30,sym)
    return inner
