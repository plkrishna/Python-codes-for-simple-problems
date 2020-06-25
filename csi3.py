#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:41:14 2019

@author: plkrishna2211
"""

st=[]
c=0
max1=0
l=[]
while True:
    n=int(input())
    if n<0:
        break
    l.append(n)
for i in range(1,len(l)):
    if l[i]<=l[i-1]:
        c+=1
        st.append(l[i-1])
    else:
        if(c>1):
            st.append(l[i-1])
            maxv=st[-1]-st[0]
            if(maxv<max1):
                max1=maxv
                le=len(st)
            st=[]
            c=0
print(le)