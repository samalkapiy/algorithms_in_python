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
'''
#2. Permutations

def permute(string, pocket=" "):  
    global count        
    if len(string) == 0:            # another method: if string == "":
        print(pocket) 
        count = count + 1
    else:
        for i in range((len(string))):
            letter = string[i]
            front = string[0:i]             
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket )
count = 0
string = str(input("Insert the string for which you need to find the permutations:"))
permute(string, " ")
print("Number of permutations: %d"%count)
'''

#3. Fibonnaci sequence

n = int(input("How many elements of the fibbonachi sequence do you want to print?:"))

def fib(n):
    if n == 1:
        return 0
    elif (n==2):
        return 1
    else:
        return fib(n-1) + fib (n-2)

#print(fib(n))


seq=[]

def fib_seq(n):
    #seq = np.zeros(n)
    for i in range(1,n+1):
        result = fib(i)
        print(result)
        seq.append(result)
    #print(fib(n))

fib_seq(n)
print(seq)


