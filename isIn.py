#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:13:32 2018

@author: zhangruiqi
"""

def isIn(char, aStr):
    '''
    aStr: an alphabetical string
    '''
    if aStr == '':
        return False
    if len(aStr) == 1:
        return aStr == char
    
    midIndex = len(aStr)//2
    midChar = aStr[midIndex]
    if char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])