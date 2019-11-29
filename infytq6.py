#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:46:20 2019

@author: plkrishna2211
"""
bill_amount=0
typ=input('Type of Food:')
dist=int(input('Enter distance:'))
quantity=int(input('Quantity:'))
if (typ!='V' and typ!='N') or quantity<1 or dist<0:
    print('Bill amount:-1')
else:
    if typ=='V':
        bill_amount+=120*quantity
    else:
        bill_amount+=150*quantity
    if dist>3 and dist<6:
        bill_amount+=(dist-3)*3
    elif dist>6:
        bill_amount+=9+(dist-6)*6
    print('Bill amount:{}'.format(bill_amount))
