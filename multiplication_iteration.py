#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:01:10 2018

@author: zhangruiqi
"""

def multiply(a,b):
    result = 0
    while b > 0:
        result = result + a
        b -= 1
    return result