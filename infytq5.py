#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:58:04 2019

@author: plkrishna2211
"""
currency=input("Currency:")
inr=int(input('INR:'))
if currency=='Euro':
    print('Currency required:{} {}s'.format(inr*0.01417,currency))
elif currency=='British Pound':
    print('Currency required:{} {}s'.format(inr*0.100,currency))
elif currency=='Australian Dollar':
    print('Currency required:{} {}s'.format(inr*0.02140,currency))
elif currency=='Canadian Dollar':
    print('Currency required:{} {}s'.format(inr*0.02027,currency))
else:
    print('-1')
