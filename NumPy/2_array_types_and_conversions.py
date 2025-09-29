import numpy as np

intergers = np.array([10,20,30,40,50])
print(intergers) # [10 20 30 40 50]

print(f"first element => {intergers[0]}")  # first element => 10

intergers[0] = 20
print(intergers) # [20 20 30 40 50]

## assigning floating point value
intergers[1] = 32.78
print(intergers) # [20 32 30 40 50] --- it has truncated the value to 32

## data type should be same
print(intergers.dtype)

intergers = np.array([21.23, 324.45, 546.3, 35], dtype=np.float32)
print(intergers) # [ 21.23 324.45 546.3   35.  ]

print("--------------------------------------------------------------------------------------------")

## multi-dimensional arrays

nums = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(nums) 
# [[ 1  2  3  4  5]
# [ 6  7  8  9 10]]

## accessing 1
print(nums[0][0]) # 1
print(nums[1][4]) # 10

## check the dimension
print(nums.ndim) # 2

## let's create 3 dimensional array.
nums = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])
print(nums)
'''
[[
    [ 1  2  3]
    [ 4  5  6]
 ]
 [
    [ 7  8  9]
    [10 11 12]
 ]
]
'''
print(nums.ndim) # 3
## how to access elements 
print(nums[0][0][0]) # 1
print(nums[1][1][0]) # 10
# or

print(nums[0,0,0]) # 1