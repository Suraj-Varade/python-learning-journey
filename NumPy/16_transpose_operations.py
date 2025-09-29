import numpy as np

# revert or permute the axes of an array; returns the modified array.
first_2dim_arr = np.arange(1, 13).reshape((3, 4))
print(first_2dim_arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(np.transpose(first_2dim_arr))
'''
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
'''

# ---------------------------

second_2dim_arr = np.arange(6).reshape((3,2))
print(second_2dim_arr)
'''
[[0 1]
 [2 3]
 [4 5]]
'''
print(second_2dim_arr.transpose())
'''
[[0 2 4]
 [1 3 5]]
'''

# --------------------------------

three_dim_arr = np.arange(24).reshape(2,3,4)
print(three_dim_arr)
'''
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
'''
print(np.moveaxis(three_dim_arr, 0, -1))
'''
[[[ 0 12]
  [ 1 13]
  [ 2 14]
  [ 3 15]]

 [[ 4 16]
  [ 5 17]
  [ 6 18]
  [ 7 19]]

 [[ 8 20]
  [ 9 21]
  [10 22]
  [11 23]]]
'''