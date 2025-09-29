import numpy as np

## 2d array
twodim_arr = np.reshape(np.arange(1, 13), (3, 4))
print(twodim_arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
## get element - second row and second column
print(twodim_arr[1,1]) # 6
print(twodim_arr[1]) #  [ 5  6  7  8]

## 3d array
three_dim_arr = np.reshape(np.arange(1, 61), (3,4,5))
print(three_dim_arr)
'''
[[[ 1  2  3  4  5]
  [ 6  7  8  9 10]
  [11 12 13 14 15]
  [16 17 18 19 20]]

 [[21 22 23 24 25]
  [26 27 28 29 30]
  [31 32 33 34 35]
  [36 37 38 39 40]]

 [[41 42 43 44 45]
  [46 47 48 49 50]
  [51 52 53 54 55]
  [56 57 58 59 60]]]
'''
print(three_dim_arr[0,2,3]) # 14
print(three_dim_arr[0,2]) # [11 12 13 14 15]

## accessing element from the end.
print(three_dim_arr[-1])
'''
[[41 42 43 44 45]
 [46 47 48 49 50]
 [51 52 53 54 55]
 [56 57 58 59 60]]
'''

print(three_dim_arr[-1, -1, 0]) # 56
print("-------------------------------------------------------------------------------")
print("Slicing ->>>>>>") # start, end, step(optional)(how many element to jump over)
onedim_arr = np.arange(1, 11) 
print(onedim_arr) # [ 1  2  3  4  5  6  7  8  9 10]
print(onedim_arr[2:6]) # index 2 to index 6 # [3 4 5 6]
print(onedim_arr[:-2]) # [1 2 3 4 5 6 7 8]
print(onedim_arr[1:-1]) # [2 3 4 5 6 7 8 9]
print(onedim_arr[-1]) # 10
print(onedim_arr[:0]) # []
print(onedim_arr[len(onedim_arr) - 2: len(onedim_arr) - 1]) # [9]
print(onedim_arr[:5]) # first 5 elements # [1 2 3 4 5]
print(onedim_arr[-3:]) # last 3 elements # [ 8  9 10]
print(onedim_arr[-1:]) # [10]
print(onedim_arr[::2]) # every alternate number # [1 3 5 7 9]

## 2d array
print(twodim_arr)  
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(twodim_arr[1:,1:])
'''
[[ 6  7  8]
 [10 11 12]]
'''
# get second row
print(twodim_arr[1,:]) # [5 6 7 8]
