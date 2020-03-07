# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:13:44 2020

@author: ROG
"""
import random
x = "y"
status = "y"
while(x == "y"):
    a = random.randint(1,9)
    b = []
    while(status == "y"):
        user = int(input("guess number: "))
        b.append(user)
        if(user == a):
            print("very good guess")
            print(b)
            break;
        elif (user < a):
            print("you say low!")
            status = input("Do you want to continue (y/n): ")
        else:
            print("you say high!")           
            status = input("Do you want to continue (y/n): ")

    x = input("Do you want to continue (y/n): ")
