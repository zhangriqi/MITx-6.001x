#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 21:22:19 2018

@author: zhangruiqi
"""
epsilon = 0.01
x = -0.009
low = 0.0
high = abs(x)
ans = (low+high)/2.0
num_guesses = 0
while abs(ans**3 - abs(x)) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high))
    if ans**3 < abs(x):
        low = ans
    else:
        high = ans
    ans = (low+high)/2.0
    num_guesses += 1
print("Number of guesses: ", num_guesses)
if x < 0:
    print(str(-ans) + " is close to cube root of ", x)
else:
    print(str(ans) + " is close to cube root of ", x)