#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:24:44 2018

@author: zhangruiqi
"""
cube = 27
guess = 2.0
epsilon = 0.01
increment = 0.001
guess_count = 0
while abs(guess**3-cube) >= epsilon:
    guess += increment
    guess_count += 1
print("number of guesses: ", guess_count)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of ", cube)
else:
    print(guess, "is close to the cube root of ", cube)
