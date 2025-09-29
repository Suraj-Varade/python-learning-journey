import numpy as np

nums = np.arange(1, 13)
print(nums[::-1]) # [12 11 10  9  8  7  6  5  4  3  2  1]
print(np.flip(nums)) # [12 11 10  9  8  7  6  5  4  3  2  1]


arr_2_dim = np.arange(9).reshape(3,3)
print(arr_2_dim)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print(np.flip(arr_2_dim))
'''
[[8 7 6]
 [5 4 3]
 [2 1 0]]
'''
print(arr_2_dim[::-1])
'''
[[6 7 8]
 [3 4 5]
 [0 1 2]]
'''
