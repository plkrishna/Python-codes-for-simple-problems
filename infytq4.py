#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:40:59 2019

@author: plkrishna2211
"""
fiver=int(input('5 rupee coins:'))
oner=int(input('1 rupee coins:'))
amount=int(input('Amount to be paid:'))
if oner<amount%5 or oner<amount-(5*fiver):
    print('-1')
elif amount-(5*fiver)>5:
    print('5 rupee coins:{}'.format(fiver))
    print('1 rupee coins:{}'.format(amount-(5*fiver)))
else:
    print('5 rupee coins:{}'.format(amount//5))
    print('1 rupee coins:{}'.format(amount%5))
    