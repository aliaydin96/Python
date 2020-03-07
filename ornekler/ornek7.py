# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:37:55 2020

@author: ROG
"""
"""
def prime(x):
    durum = False
    for i in range(x):
        if((i != 0) & (i != 1)):
            if(x%i == 0):
                print(str(x) + " is not prime number")
                durum = True
                break
                
    if(durum == False):
        print(str(x) + " is prime number")
            

while(True):
    user = int(input("Give a number: "))
    prime(user)
"""

user = int(input("Give a number: "))
b = [user for i in range(2,user) if user%i == 0] 
if(b == []):
    print("prime number")

    
