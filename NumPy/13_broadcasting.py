import numpy as np

a = np.arange(1,10).reshape((3,3))
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(a)

b = np.arange(1, 4) # [1 2 3]
print(b)

print(a + b)
'''
[[ 2  4  6]
 [ 5  7  9]
 [ 8 10 12]]
'''
## numpy can add 2 arrays of same dimension. 

d = np.arange(1,3).reshape((1,2))
print(d) # [[1 2]]
e = np.arange(1,11).reshape((5,2))
print(e)
'''
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]]
'''

three_dim_array = np.arange(24).reshape(2,3,4)
print(three_dim_array)
'''
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
'''
one_dim_array = np.arange(4)
print(one_dim_array) # [0 1 2 3]
print(three_dim_array - one_dim_array)
'''
[[[ 0  0  0  0]
  [ 4  4  4  4]
  [ 8  8  8  8]]

 [[12 12 12 12]
  [16 16 16 16]
  [20 20 20 20]]]
'''
