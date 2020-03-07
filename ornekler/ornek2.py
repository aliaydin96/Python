# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:07:39 2020

@author: ROG
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = []
for i in range(len(a)):
    for j in range(len(b)):
        if(b[j] == a[i]):
            c.append(a[i])
for num in c:
    if num not in d:
        d.append(num)
        
print(c)
print(d)

