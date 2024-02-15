## This script contains examples of recursive algorthms in Python ##

import numpy as np
import matplotlib.pyplot as plt

#________________________________________
# Recursive algorithms

#1. Factorials
'''
num = int(input("Insert Number of which you want to find the factorial:"))

def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

facto = factorial(num)

print("Factorial of %d is:%d"%(num,facto))
'''

#2. Permutations

def permute(string, pocket=" "):          
    if len(string) == 0:
        print(pocket) 
    else:
        for i in range((len(string))):
            letter = string[i]
            front = string[0:i]             
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket )

string = str(input("Insert the string for which you need to find the permutations:"))
permute(string, " ")