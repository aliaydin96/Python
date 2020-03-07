# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:07:11 2020

@author: ROG

The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

number = 100

sum_sq = number * (number + 1) * (2 * number + 1) / 6
print(sum_sq)
sum = number * (number + 1) / 2
sq_sum = sum**2
print(sq_sum)
diff = sq_sum - sum_sq
print(diff)