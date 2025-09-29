## reshape

import numpy as np

first_arr = np.arange(1, 13) # [ 1  2  3  4  5  6  7  8  9 10 11 12]
## convert it to 2 dimension array
second_arr = np.reshape(first_arr, (3, 4))
print(second_arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
## trying with incompatible shape
'''
third_arr = np.reshape(first_arr, (15, 15)) # ValueError: cannot reshape array of size 12 into shape (15,15)
print(third_arr) 
'''

## convert the 1D array to 3D array
fourth_arr = np.reshape(first_arr, (2,3,2))
print(fourth_arr)
'''
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
'''

## Convert 2D or ND array to 1D array
fifth_arr = np.full((4,5), 8)
print(fifth_arr)
'''
[[8 8 8 8 8]
 [8 8 8 8 8]
 [8 8 8 8 8]
 [8 8 8 8 8]]
'''
fifth_arr.fill(5)
print(fifth_arr)
'''
[[5 5 5 5 5]
 [5 5 5 5 5]
 [5 5 5 5 5]
 [5 5 5 5 5]]
'''

## convert this 2D array to 1D array -- this called flattening
sixth_arr = np.reshape(fifth_arr, -1)
print(sixth_arr) # [5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5]
seventh_arr = np.reshape(first_arr, -1)
print(seventh_arr) # [ 1  2  3  4  5  6  7  8  9 10 11 12]

print("----------------------------------------------------------------------")
## there are 2 ways to flatten the array.
# flatten ->> create a copy (any changes to new array won't impact the other)
# ravel ->> create a view (any change to one, impact other)

a_array = np.array([[10,20,30], [40, 50, 60], [70, 80, 90]])

eighth_arr_flat = np.ndarray.flatten(a_array) 
# this will create a new copy, so changing one, don't impact another one.
print(eighth_arr_flat) # [10 20 30 40 50 60 70 80 90]
a_array[2][0] = 110
print(a_array) 
'''
[[ 10  20  30]
 [ 40  50  60]
 [110  80  90]]
'''
print(eighth_arr_flat) # [10 20 30 40 50 60 70 80 90]
## no changes.
print("---------------------------------------------------------------------------")

## let's check with ravel - it will create another array but a shallow copy
b_array = np.array([[1,2], [4,5]])
nineth_array = np.ndarray.ravel(b_array)
print(b_array)
'''
[[1 2]
 [4 5]]
'''
print(nineth_array) # [1 2 4 5]

## let's try to change the value 
b_array[1,1] = 7
print(b_array)
'''
[[1 2]
 [4 7]]
'''
print(nineth_array) # [1 2 4 7]