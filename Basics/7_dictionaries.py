result = {"key" : "value"}
print(result)

## key has to be unique, there can't be duplicates
result = {1 : "abc", 2 : "xyz", 1: None, 2 : "abcd"}
print(result) # {1: None, 2: 'abcd'}

