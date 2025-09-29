import numpy as np

## adding number
integers = np.array([1,2,3,5])
## add element 4 in index 3
new_integers = np.insert(integers, 3, 4) # adding 3 at index 4
print(new_integers) # [1 2 3 4 5]

## append element.
second_arr = np.append(new_integers, 6)
print(second_arr) # [1 2 3 4 5 6]
print(new_integers) # [1 2 3 4 5]

## delete element
third_arr = np.array([5,3,3,2,1])
new_third_arr = np.delete(third_arr, 4) # element to be removed from specific index
print(new_third_arr) # [1 2 3 4]

new_sorted_arr = np.sort(new_third_arr, 0)
print(new_sorted_arr) # [2 3 3 5]

## sort 2 dim array
integers_2_dim_arr = np.array([[1,4,3,5,2],[18,2,3,47,3]])
print(integers_2_dim_arr)
'''
[[ 1  4  3  5  2]
 [18  2  3 47  3]]
'''

integers_2_dim_sort_arr = np.sort(integers_2_dim_arr)
print(integers_2_dim_sort_arr)
'''
[[ 1  2  3  4  5]
 [ 2  3  3 18 47]]
'''

## sort array of strings
colors = np.array(["red", "yellow", "green", "blue", "brown", "black", "white"])
print(np.sort(colors)) # ['black' 'blue' 'brown' 'green' 'red' 'white' 'yellow']