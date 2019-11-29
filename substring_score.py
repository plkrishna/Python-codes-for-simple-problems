#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:01:36 2019

@author: plkrishna2211
"""
ip=input()
v_sco,c_sco=0,0
l=len(ip)
vowels='aeiou'
for i in range(l):
    if ip[i] in vowels:
        v_sco+=l-i
    else:
        c_sco+=l-i
if v_sco>c_sco:
    print('Vowel')
else:
    print('Consonant')
