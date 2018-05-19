#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 08:42:58 2018

@author: zhangruiqi
"""

def printMove(fr, to):
    print("Move from " + str(fr) + " to " + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        '''
        First move the stack of n-1 size to the spare swap
        Then move the last piece to the spot
        Then move the stack of n-1 on spare to the spot
        '''
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
print(Towers(4, 'P1', 'P2', 'P3'))
