#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:54:24 2018

@author: zhangruiqi
"""

num = -3
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result += str(num % 2)
    num = num // 2
if isNeg:
    result = '-' + result

