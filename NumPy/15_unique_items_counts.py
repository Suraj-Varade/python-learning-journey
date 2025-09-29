import numpy as np

nums = np.array([2,3,6,3,4,8,9,6,6,2,4,9,0,34,0])
nums.sort() # [ 0  0  2  2  3  3  4  4  6  6  6  8  9  9 34]
print(nums) 
print("removed duplicates : ", set(nums))
# removed duplicates :  {np.int64(0), np.int64(2), np.int64(3), np.int64(4), np.int64(34), np.int64(6), np.int64(8), np.int64(9)}

print(np.unique(nums)) # all unique # [ 0  2  3  4  6  8  9 34]

second_arr = np.array([[1,1,2,1], [3,1,4,1], [1,1,2,1], [7,1,1,1]])
print(second_arr)
'''
[[1 1 2 1]
 [3 1 4 1]
 [1 1 2 1]
 [7 1 1 1]]
'''
print(np.unique(second_arr)) # [1 2 3 4 7]
print(np.unique(second_arr, axis=0))
'''
[[1 1 2 1]
 [3 1 4 1]
 [7 1 1 1]]
'''

## returning indexes
print(nums) # [ 0  0  2  2  3  3  4  4  6  6  6  8  9  9 34]
print(np.unique(nums)) # [ 0  2  3  4  6  8  9 34]
print(np.unique(nums,return_index=True))
# (array([ 0,  2,  3,  4,  6,  8,  9, 34]), array([ 0,  2,  4,  6,  8, 11, 12, 14]))

## freq. count
print(np.unique(nums, return_counts= True))
# (array([ 0,  2,  3,  4,  6,  8,  9, 34]), array([2, 2, 2, 2, 3, 1, 2, 1]))

print(np.unique(nums, return_inverse= True))
# (array([ 0,  2,  3,  4,  6,  8,  9, 34]), array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7]))