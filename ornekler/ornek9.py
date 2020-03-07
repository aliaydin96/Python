# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:09:16 2020

@author: ROG
"""
user = input("Give a sentence: ")
a = user.split()
print(a)
b = a[::-1]
b = " ".join(b)
print(b)
