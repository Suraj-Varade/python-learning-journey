import numpy as np

## concatenate
first_arr = np.arange(1, 11)
second_arr = np.arange(11, 21)
print(f"first array = {first_arr}, \n second array = {second_arr}")
'''
first array = [ 1  2  3  4  5  6  7  8  9 10], 
 second array = [11 12 13 14 15 16 17 18 19 20]
'''
con_arr = np.concatenate((first_arr, second_arr))
print(con_arr) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
print(np.reshape(con_arr, (2, 2, 5)))
'''
[[[ 1  2  3  4  5]
  [ 6  7  8  9 10]]

 [[11 12 13 14 15]
  [16 17 18 19 20]]]
'''
## reversing the array
print(con_arr[::-1]) # [20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1]
print(np.flip(con_arr)) # [20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1]

# print(np.concatenate((first_arr, second_arr)))

## stack
str_arr = np.stack((first_arr, second_arr))
print(str_arr)
'''
[[ 1  2  3  4  5  6  7  8  9 10]
 [11 12 13 14 15 16 17 18 19 20]]
'''
hst_arr = np.hstack((first_arr, second_arr))
print("hstack", hst_arr) # hstack [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]

vst_arr = np.vstack((first_arr, second_arr))
print("vstack", vst_arr) 
'''
vstack [[ 1  2  3  4  5  6  7  8  9 10]
 [11 12 13 14 15 16 17 18 19 20]] 
'''

## functions for splitting arrays.
## splitting breaks one array to multiple subarrays
## resulting subarrays should be properly divisible by the number otherwise it will throw an error.

fifth_arr = np.arange(1, 13)
sp_arr = np.array_split(fifth_arr, 4)

print(sp_arr) # [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9]), array([10, 11, 12])]

print(sp_arr[1]) # [4, 5, 6]

print(np.array_split(fifth_arr, 8))
# [array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8]), array([9]), array([10]), array([11]), array([12])]

print(np.array_split(fifth_arr, 4)) # [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9]), array([10, 11, 12])]

