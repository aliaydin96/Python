# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:55:08 2020

@author: ROG
"""
a = [i for i in range(10)]
b=[]
i=0
while(i<len(a)):
    if(a[i]<5):
        b.append(a[i])
    i+=1
print(b)