## string
summary = 'my name is john'
print(summary) # my name is john

## what if i want to put "john" in quote
summary = 'my name is "john"'
print(summary) # my name is "john"

## what if i want to add single and double quote
summary = """my name is 'john', i am doing "great!!"."""
print(summary) # my name is 'john', i am doing "great!!".

## composing new string
summary = summary + ", welcome to the team 'John :)'"
print(summary) # my name is 'john', i am doing "great!!"., welcome to the team 'John :)'

## use f-strings to replace variable in a string
name = "steve"
result = f"{name} is teaching f-strings!!"
print(result) # steve is teaching f-strings!!

print("-------------------------------------------------------------------")

## Integers
age = 15
print(type(age)) # <class 'int'>

result = age / 2
print(result) # 7.5

result = f"I am a {age} years old"
print(result) # I am a 15 years old

#7 + "14" # mixing unsupported types
val = 7 + int("14")
print(val) # 21

## invalid math operations - divide by zero
#invalidMath = age / 0
#print(invalidMath) # ZeroDivisionError: division by zero

## data type will get changed
a = 21
b = 42
c = a + b
print(f"{c} - and type : {type(c)}") # 63 - and type : <class 'int'>
d = c / 2
print(f"{d} - and type : {type(d)}") # 31.5 - and type : <class 'float'>

print("-------------------------------------------------------------------")

## float
print(type(15.4)) # <class 'float'>

f = 32 / 5
print(f"result is : {f} of type : {type(f)}") # result is : 6.4 of type : <class 'float'>

k = 30 / 3
print(f"result is : {k} of type : {type(k)}") # result is : 10.0 of type : <class 'float'>

intVal = 21
intVal = k
print(f"{intVal}" + " - " + f"{type(intVal)}") # 10.0 - <class 'float'>

pi = 311 / 99
print(pi) # 3.1414141414141414
print(f"{pi}") # 3.1414141414141414
pi_2_decimal = f"{pi:.2f}"
print(pi_2_decimal, type(pi_2_decimal)) # 3.14 <class 'str'>

pi_2_decimal = round(pi, 2)
print(pi_2_decimal) # 3.14

print("-------------------------------------------------------------------")

print("type of bool", type(True)) # type of bool <class 'bool'>

first_result = bool(1)
second_result = bool(0)
print(f"{first_result}, {second_result}") # True, False

isSuccess = True

print("-------------------------------------------------------------------")

print(type(None)) # <class 'NoneType'>


