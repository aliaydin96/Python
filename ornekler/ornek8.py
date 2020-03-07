# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:58:53 2020

@author: ROG
"""
def fibonacci(x):
    a = []
    for i in range(x):
        if(i == 0):
            a.append(1)
        elif(i == 1):
            a.append(1)
        else:
            a.append(a[i-2] + a[i-1])

    return a
        
user = int(input("length: "))
a = fibonacci(user)
print(a)