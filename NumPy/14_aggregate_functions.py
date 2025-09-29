import numpy as np

first_arr = np.arange(1, 11)
print(f"Sum => ", np.sum(first_arr)) # Sum =>  55

## calculate the sum of all even numbers.
print(first_arr[::2]) # [1 3 5 7 9]
print(first_arr[::-2]) # [10  8  6  4  2]
print(first_arr[first_arr % 2 == 0]) # [ 2  4  6  8 10]
print(np.sum(first_arr[first_arr % 2 == 0])) # 30

## 2 D
second_arr = np.arange(1,26).reshape(5, 5)
print(second_arr)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
'''
print(sum(second_arr)) # [55 60 65 70 75]

## 2 D
third_arr = np.arange(1, 13).reshape((3, 4))
print(third_arr)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print(sum(third_arr)) # [15 18 21 24]

## things are slightly different, when we use sum() function in different way.
print(first_arr.sum()) # 55
print(second_arr.sum()) # 325 
print(third_arr.sum()) # 78

print(third_arr.sum(axis= 0)) # [15 18 21 24]
print(third_arr.sum(axis= 1)) # [10 26 42]

print("--------------------------------------------------------------------------------")
print(third_arr.prod()) # 479001600

print("Min : ", np.min(first_arr), "Max : ", np.max(first_arr)) 
# Min :  1 Max :  10
print("Min : ", np.min(third_arr), "Max : ", np.max(third_arr))
# Min :  1 Max :  12
print("Average : ", np.average(third_arr)) # 6.5
print("Mean (first_arr): ", first_arr.mean()) # 5.5
print("Mean (third_arr): ", third_arr.mean(axis = 0)) # [5. 6. 7. 8.]
print("Mean (third_arr): ", third_arr.mean(axis = 1)) # [ 2.5  6.5 10.5]