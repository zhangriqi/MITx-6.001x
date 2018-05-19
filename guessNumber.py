#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:04:50 2018

@author: zhangruiqi
"""

print("Please think of a number between 0 and 100!")
epsilon = 1
low = 0
high = 100
s = ""
while True:
    ans = int((low+high)/2)
    print("Is your secret number " + str(ans) + " ?")
    s = input("Enter 'h' to indicate the guess is too high.\
              'l' to indicate the guess is too low.\
              Enter 'c' to indicate I guessed correctly.")
    if s == 'l':
        low = ans
    elif s == 'h':
        high = ans
    elif s == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:", ans)