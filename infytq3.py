#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:24:43 2019

@author: plkrishna2211
"""
level=int(input('Level:'))
salary=int(input('Salary:'))
if level==3:
    salary=salary+salary*0.15
elif level==4:
    salary=salary+salary*0.07
elif level==5:
    salary=salary+salary*0.05
else:
    pass
print('Incremented Salary:{}'.format(salary))