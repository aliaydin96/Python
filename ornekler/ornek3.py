# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:33:43 2020

@author: ROG
"""

str_in = input("string: ")
str_pol =""
for i in range(len(str_in)):
    str_pol = str_pol + str_in[len(str_in) - i-1]
    
if(str_pol == str_in):
    print(str_pol + " is polidrom")