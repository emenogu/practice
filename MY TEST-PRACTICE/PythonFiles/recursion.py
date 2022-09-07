## 1. Recursion is a function calling itself
import sys
from typing import Sequence
sys.setrecursionlimit(50)
print(sys.getrecursionlimit())
i = 0

def greet():
    global i
    i+=1
    print('Hello ', i)
    greet()
#greet()



## 2. Calculating Factorials
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

result = fact(5)
print(result)

# 3. Using filter() function
# filter(names, pattern)
def is_even(n):
    return n%2==0
    
nums = [3,6,2,7,3,9,5,4,6,7,8,1,0, 6, 8]
evens = list(filter(is_even, nums)) # or
evens = list(filter(lambda n : n%2==0, nums))
print(evens)
print('There are', len(evens), 'even numbers available')
print()

# 4. Maps()
# map(function, iterables)
from functools import *
double = list(map(lambda m : m+m, evens))

# Reduce()
sum = reduce(lambda a,b:a+b, nums) 
print(double)
print('The sum of all the original numbers is', sum)

