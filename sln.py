# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:01:25 2022

@author: acer
"""

for num in range(1,100):
    string = ""
    if num % 5 == 0 and num % 3 == 0:
        string = string + "Fizzbuzz"
    elif num % 5 == 0:
        string = string + "Buzz"
    elif num % 3 == 0:
        string = string + "Fizz"
    else:
        string = string + str(num)
    print(string)