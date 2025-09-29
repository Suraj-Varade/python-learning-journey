import numpy as np

## array of all zeros
arr_of_all_zeros = np.zeros(5)
print(arr_of_all_zeros) # [0. 0. 0. 0. 0.]

print(np.zeros((4,5))) # 2 dim array filled with zeros, default data type is floating point
'''
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
'''

## array of all ones
print(np.ones((4, 5))) # default datatype is floating point
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''
print(np.ones((4,5), dtype=int)) # change data type to int
'''
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
'''

## fill, full
first_fill_array = np.empty(10, dtype=int)
print(first_fill_array) # [0 0 0 0 0 0 0 0 0 0]

print(np.empty(1, dtype=int)) # [0]

# let's fill the array now.
first_fill_array.fill(2)
print(first_fill_array) # [2 2 2 2 2 2 2 2 2 2]

first_full_array = np.full(5, 10)
print(first_full_array) # [10 10 10 10 10]

second_full_array = np.full((4,5), 8)
print(second_full_array) 
'''
[[8 8 8 8 8]
 [8 8 8 8 8]
 [8 8 8 8 8]
 [8 8 8 8 8]]
'''