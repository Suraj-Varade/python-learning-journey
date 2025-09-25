import math

def simple():
    print("this is a function")

simple() # this is a function
print(simple()) # None

def check_if_num_is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for number in range(2, int(math.sqrt(num)) + 1):
        if num % number == 0:
            return False
    return True

num = 5
result = check_if_num_is_prime(num)
print(f"is {num} a prime number ? => {result}")

## function to take 0 or more arguments
def calculate_total_sum(*items):
    total_sum = 0
    for item in items:
        total_sum += item
    print(total_sum)
    return total_sum

calculate_total_sum(21,43,35,6,7,8,94345,23) # 94488

## function to take 0 or more types of arguments
def print_collection(*items):
    for item in items:
        print(item)

print_collection(21,324,2,"3425",True, 342.45, 334)

## act like a dictionary.
def stats(**dictItems):
    for key, value in dictItems.items():
        print(key, " --->> ", value)

stats(speed = "slow", active = False, weight = 340)
'''
speed  --->>  slow
active  --->>  False
weight  --->>  340
'''