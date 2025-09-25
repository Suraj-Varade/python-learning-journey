items = []
print(items) # []

items_1 = list()
print(items_1) # []

colors = ["red", "yellow", "blue", "brown", "white", "black"]
output = ""
for color in colors:
    print(color)
    output += f" {color}"

print(output.strip()) # red yellow blue brown white black
# strip is to remove leading and trailing whitespaces. - similar to trim in c#

## to get the index also along with the values
for index, value in enumerate(colors):
    print(index + 1, ":" , value)

'''
1 : red
2 : yellow
3 : blue
4 : brown
5 : white
6 : black
'''

'''
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''
## FizzBuzz - range
result = []
n = 5
for num in range(1,n + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        result.append("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
        result.append("Fizz")
    elif num % 5 == 0:
        print("Buzz")
        result.append("Buzz")
    else:
        print(num)
        result.append(f"{num}")

print("----------------------------------------------------------------")

## list comprehensions
numbers = [2,3,4,12,5,3,4]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers) # [2, 4, 12, 4]

