#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 14:24:56 2019

@author: plkrishna2211
"""

def processArray(li):
  if li==[]:
    return 0
  return max(li)

li=[]
while True:
  k=int(input())
  if k<0:
    break
  else:
    if k%2!=0:
      li.append(k)
print(processArray(li))