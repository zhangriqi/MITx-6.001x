#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 08:55:23 2018

@author: zhangruiqi
"""

def gcditer(a,b):
    gcd = min(a,b)
    
    while a%gcd != 0 or b%gcd != 0:
        gcd -= 1
    return gcd

def gcdRecur(a,b):
    if a == 0:
        return b
    else:
        return gcdRecur(b%a, a)
    
    
print (gcdRecur(12,9))