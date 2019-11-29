# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:36:33 2019

@author: win
"""
st='''this is alpha
beta gama zeno
welcome to world
the world of zeno'''
alphabets='abcdefghijklmnopqrstuvwxyz'
d={k:st.count(k) for k in alphabets}
print(d)
print(max(d.items(),key=lambda x:x[1]))
print(min(d.items(),key=lambda x:x[1]))

l=sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in range(3):
    print(l[i][0])

di=dict().fromkeys(list(alphabets),0)
for k in st:
    if k in di.keys():
        di[k]=di[k]+1
print(di)

dis={}
for k in st:
    if k in alphabets:
        dis.update({k:dis.setdefault(k,0)+1})
