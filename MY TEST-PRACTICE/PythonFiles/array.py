# from array import *
# import numpy
from numpy import *

# vals = array('i',[5, -8, 9, 2, 1] )
# # vals.reverse()

# for i in range(len(vals)):
#     print(vals[i], end=' ')

# print()
# newVals = array(vals.typecode, (a for a in vals))    
# for e in newVals:
#     print(e, end=' ')


# arr = array('i', [])
# n = int(input('How many values do you want to enter? '))

# for i in range(n):
#     x = int(input('Enter the values '))
#     arr.append(x)
# for a in arr:
#     print(a, end=' ')
# print()
# #To search for a value
# val = int(input('Enter the Value to search '))
# print()
# for a in arr:
#     if a == val:
#         print(val, 'is present')
        
# print(val, 'is located in index position', arr.index(val))

# arr = array([1, 2, 4, 5, 6])
# arr1 = linspace(0, 5, 6) ##The gap btween any two element is fixed
# arr2 = arange(0, 6)
# arr3 = logspace(0, 5, 6) ## The gap depends on the log of it.
# arr4 = ones(5)
# arr5 = zeros(5)
# print(arr1)
# print(arr3)
# # print('%.2f' %arr3[1])
# print(arr4)
# print(arr5)

    # Copying Arrays
arr5 = array([1, 2, 3, 4, 5])
arr6 = array([2, 4, 6, 8, 10])
# arr7 = arr5.view()
# arr8 = arr5.copy()
# # print(concatenate([arr5, arr6]))
# arr5[0] = 9
# print(arr7)
# print(id(arr7))
# print(arr8)
# print(id(arr8))
print()
arr9 = array([
            [1, 2, 3, 4, 13],
            [5, 6, 7, 8, 14],
            [9, 10, 11, 12, 15]
        ])
# print(arr9)
print(arr9.ndim)
print()
m1 = matrix(arr5)
m2 = matrix(arr9)
m3 = m1 - m2
print(m3)