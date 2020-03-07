# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:23:25 2020

@author: ROG

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
sum = 0
liste = []
for i in range(1000):
    if(i%3 == 0):
        liste.append(i)
        sum = sum + i
    elif(i%5 == 0):
        liste.append(i)
        sum = sum + i
    
print(liste)

print(sum)
