import numpy as np # numpy

## convenient to use
## faster than list
## Fixed size once created → you cannot directly append or remove.
## If you try to "append", NumPy actually creates a new array in memory 
## (slower for frequent inserts/removals).
## This is why NumPy is fast for mathematical operations but not ideal for dynamic data.

integers = np.array([10,20,30,40,50])
print(integers) # [10 20 30 40 50]
print(integers[0]) # 10

integers[0] = 20
print(integers) # [20 20 30 40 50]

integers[0] = 21.5
print(integers) # [21 20 30 40 50] - because all the data should be of same type
## type safety

print(integers.dtype) # int64

## you can change the dtype of an nparray
small_integers = np.array([45,88,34,21,89], dtype=np.int32)
print(small_integers) # [45 88 34 21 89]

## check the memory.
print(integers.nbytes) # 40
print(small_integers.nbytes) # 20

## working on memory consumptions.
floats = np.array([23,34,4.5,3,24,5]) 
print(floats) # [23.  34.   4.5  3.  24.   5. ]
print(floats.nbytes) # 48
print(floats.dtype) # float64

