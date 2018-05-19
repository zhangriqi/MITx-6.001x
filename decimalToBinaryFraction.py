#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:32:56 2018

@author: zhangruiqi
"""

x = float(input("Enter a decimal number between 0 and 1:"))

p = 0
while (x*(2**p)) % 1 != 0:
    print ("Remainder = " + str(x*(2**p)- int(x*(2**p))))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result += str(num % 2)
    num = num // 2

for i in range(p - len(result)+1):
    result = '0' + result
result = result[0:-p] + '.' + result[-p:]

print("The binary form of " + str(x) + " is " + str(result))
    