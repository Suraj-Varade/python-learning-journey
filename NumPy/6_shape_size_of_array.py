import numpy as np

integers = np.array([[1,2,3,4,5], [6,7,8,9,10]])
## finding size and shape of an array
print(f"size of an array => {integers.size}") # 10
print(f"shape of an array => {integers.shape}") # (2, 5)
print(f"dimesion of an array => {integers.ndim}") # 2
print(f"dtype of an array => {integers.dtype}") # int64

first_arr = np.arange(20)
print(first_arr) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(f"size of first_arr => {first_arr.size}") # 20
print(f"shape of first_arr => {first_arr.shape}") # (20, )
print(f"dimesion of first_arr => {first_arr.ndim}") # 1
print(f"dtype of first_arr => {first_arr.dtype}") # int64

second_arr = np.linspace((1,2), (10, 20), 10)
print(second_arr)
'''
[[ 1.  2.]
 [ 2.  4.]
 [ 3.  6.]
 [ 4.  8.]
 [ 5. 10.]
 [ 6. 12.]
 [ 7. 14.]
 [ 8. 16.]
 [ 9. 18.]
 [10. 20.]]
'''
print(f"size of second_arr => {second_arr.size}") # 20
print(f"shape of second_arr => {second_arr.shape}") # (10, 2)
print(f"dimesion of second_arr => {second_arr.ndim}") # 2
print(f"dtype of second_arr => {second_arr.dtype}") # float64


third_arr = np.full((2,2,2), 10)
print(third_arr)
'''
[[[10 10]
  [10 10]]

 [[10 10]
  [10 10]]]
'''

print(f"size of third_arr => {third_arr.size}") # 8
print(f"shape of third_arr => {third_arr.shape}") # (2, 2, 2)
print(f"dimesion of third_arr => {third_arr.ndim}") # 3
print(f"dtype of third_arr => {third_arr.dtype}") # int64