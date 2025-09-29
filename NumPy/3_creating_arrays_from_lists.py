import numpy as np

first_list = [1,2,3,4,5,6,7,8,9,10]
print(first_list)

first_array = np.array(first_list)
print(first_array) # [ 1  2  3  4  5  6  7  8  9 10]

second_list = [1, True, "hello", 4, 5, 6]
second_array = np.array(second_list)
print(second_array) # ['1' 'True' 'hello' '4' '5' '6']
print(second_array.dtype) # <U21

third_list = [21,32,45.45,67.23,67]
third_array = np.array(third_list)
print(third_array) # [21.   32.   45.45 67.23 67.  ]
print(third_array.dtype) # float64

first_tuple = (1,2,3,4,5)
array_from_tuple = np.array(first_tuple)
print(array_from_tuple) # [1 2 3 4 5]
array_from_tuple[0] = 123
print(array_from_tuple) # [123   2   3   4   5]

## let's try to update value in tuple
print(first_tuple[0]) # 1
print(first_tuple) 

try:
    first_tuple[0] = 123  # TypeError: 'tuple' object does not support item assignment
    print(first_tuple)
except TypeError as error:
    print(error)
finally:
    print("tuples are readonly..")

multi_dim_list = [[[0,1,2], [3,4,5]], [[6,7,8],[9,10,11]]]
arr_from_multi_dim_list = np.array(multi_dim_list)
print(arr_from_multi_dim_list)
print(arr_from_multi_dim_list.dtype) # int64
print(arr_from_multi_dim_list.ndim) # 3

## if i update the number 10 to False in multi_dim_list -->> the arr_from_multi_dim_list - dtype would be object
## if i update the number 10 to "123" in multi_dim_list -->> the arr_from_multi_dim_list - dtype would be <U21, 
## but all elements would be converted into string

