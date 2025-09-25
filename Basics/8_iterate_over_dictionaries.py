contact_info = {}
print(contact_info) # {}
print(type(contact_info)) # <class 'dict'>
contact_info = dict()
print(contact_info) # {}

contact_info = {
    "id": 1,
    "name": "John",
    "address": "LA",
    "mobile" : 8888888888,
    "zip" : 40134
}

# print(contact_info)
user_info = [(1, "john"),(2, "steve"), (3, "kent"), (4, "rocky")]
print(user_info) # [(1, 'john'), (2, 'steve'), (3, 'kent'), (4, 'rocky')]
print(type(user_info)) # <class 'list'>
print(type(dict(user_info))) # <class 'dict'>

## looping over dictionaries
## only keys
for key in contact_info.keys():
    print(key)
'''
id
name
address
mobile
zip
'''
## only values
for values in contact_info.values():
    print(values)
'''
1
John
LA
8888888888
40134
'''

## get key and value both
for item in contact_info:
    print(f"{item}") # this is also returning keys - by default
    print(f"{contact_info[item]}") # to get the value

## another way to get both key and values
for key, value in contact_info.items():
    print(f"{key} - {value}")

'''
id - 1
name - John
address - LA
mobile - 8888888888
zip - 40134
'''

print(contact_info.items()) # dict_items([('id', 1), ('name', 'John'), ('address', 'LA'), ('mobile', 8888888888), ('zip', 40134)])