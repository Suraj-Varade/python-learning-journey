# variable and assignments
# it is not strongly typed.
first_name = "suraj"
last_name = "varade"
mobile_number = 88888888888 # unlike other languages, 
# python does not inherent length or maximum value of int datatype.

# get type : <class 'int'>
print(f"get type : {type(mobile_number)}") 

# get complete info : suraj - varade - 8888888888
print(f"get complete info : {first_name} - {last_name} - {mobile_number}")

# creating a full name : suraj varade
full_name = f"{first_name} {last_name}"
print(f"creating a full name : {full_name}")

# watch out for copying variables
new_name = first_name
print(f"watch out for copying variables : {new_name}") #suraj
first_name = "sagar"
print(f"watch out for copying variables : {new_name}") #suraj
print(f"watch out for copying variables : {first_name}") #sagar

# print - it adds separations when using commas
# sagar varade has started learning python
print(first_name, last_name, "has started learning python")