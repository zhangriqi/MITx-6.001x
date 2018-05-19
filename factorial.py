#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:09:27 2018

@author: zhangruiqi
"""

def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def fact_recu(n):
    if n == 1:
        return 1
    else:
        return n*fact_recu(n-1)