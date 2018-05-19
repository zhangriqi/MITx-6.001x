#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:43:53 2018

@author: zhangruiqi
"""
epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (guess**2-y)/(2*guess)
print("numGuesses = " + str(numGuesses))
print("Square root of " + str(y) + " is about " + str(guess)) 
