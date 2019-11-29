#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:42:21 2019

@author: plkrishna2211
"""
mileage=int(input('Enter mileage:(km/litre):'))
rate=int(input("Rate of fuel(Rs/litre):"))
dist=int(input('Distance:'))
cost=(rate*((dist*2)/mileage))/4
print(cost,'True',sep='\n') if cost%5==0 else print(cost,'False',sep='\n')