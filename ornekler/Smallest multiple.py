# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 21:59:31 2020

@author: ROG

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
number = 1
counter = 0
while(True):
    counter = 0
    for i in range(11, 21):
        if(number%i != 0):
            counter = counter + 1
            break
    number = number + 1
    if(counter == 0):
        print(number-1)
        break
    
    
    