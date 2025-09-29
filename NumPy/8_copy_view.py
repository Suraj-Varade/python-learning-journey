import numpy as np

students_ids_number = np.array([111,112,113,114,115,116,117,119,118])
print(students_ids_number)
students_ids_number = np.sort(students_ids_number)
print(students_ids_number) # [111 112 113 114 115 116 117 118 119]

students_ids_number_reg = students_ids_number
print(students_ids_number_reg)

students_ids_number_reg[0] = 3020
print(students_ids_number_reg) # [3020  112  113  114  115  116  117  118  119]
print(students_ids_number) # [3020  112  113  114  115  116  117  118  119]
## as both having the same memory address.

print("----------------------------------------------------------------------------")
## copy 
print("Deep copy")
students_ids_number_copied = students_ids_number.copy()
students_ids_number[0] = 2324
print(f"{students_ids_number}") # [2324  112  113  114  115  116  117  118  119]
print(f"{students_ids_number_copied}") # [3020  112  113  114  115  116  117  118  119]

print("-----------------------------------------------------------------------------")
## equality
print("Check Equality")
print(students_ids_number_copied == students_ids_number)
# [False  True  True  True  True  True  True  True  True]

print("-------------------------------------------------------------------------------")
print("Check Memory Location")
print(id(students_ids_number)) # 4433484976
print(id(students_ids_number_copied)) # 4354307824
## as you can see both have different memory location.

print("-------------------------------------------------------------------------------")
print("View")
students_ids_number_view = students_ids_number.view()
print("original", students_ids_number) # [2324  112  113  114  115  116  117  118  119]
print("view", students_ids_number_view) # [2324  112  113  114  115  116  117  118  119]
## what if i changed the value in students_ids_number array
students_ids_number[3] = 33333
print("original : ", students_ids_number) # [ 2324   112   113 33333   115   116   117   118   119]
print("view : ", students_ids_number_view) # [ 2324   112   113 33333   115   116   117   118   119]

print("compare both array", students_ids_number == students_ids_number_view)
# compare both array [ True  True  True  True  True  True  True  True  True]
print("---------------------------------------------------------------------------------")

print(students_ids_number_copied.base) # None (has it's own data) - newMemory
print(students_ids_number.base) # None (has it's own data) - original
print(students_ids_number_view.base) # points to arr : [ 2324   112   113 33333   115   116   117   118   119]