import sympy as sym 
import numpy as np

from sympy.printing.pretty import pretty_print

lst = [1,2,4,7,3,5,7,3,5,7,8,2,4,5,8]

print(lst[-2:]) # slice last 2 elements in the list
print(lst[:2]) # slice first 2 elemens in the list

n = 3
k = 7

print(lst[n:k]) #slice elements from n to k

words = ['hello', 'my', 'name','is','Gautham']

for i in words:
    print(i)
    
alist = [1 , 2, 'rain', [6,4]]

for i in alist:
    print(i)

print(alist[-1][1])