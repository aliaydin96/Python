# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:42:00 2020

@author: ROG

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
number = 600851475143
liste = []
i = 2
while(i <= number):
    if(number % i == 0):
        number = number / i
        liste.append(i)
    else:
        i = i + 1

    
print(liste)
