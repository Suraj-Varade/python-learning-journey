contact_info = {}

## since the key is not available - it will through an error (keyError)
# contact_info["name"] # keyError

try:
    contact_info["phone"]
except KeyError as error:
    print(f"key error => {error}")
except Exception as generic_exception:
    print(f"generic exception => {generic_exception}")

contact_info = dict([(1, "abc"), (2, "xyz"), (3, "ops")])
print(contact_info) # {1: 'abc', 2: 'xyz', 3: 'ops'}

print(type(contact_info)) # <class 'dict'>
if 1 in contact_info:
    print(contact_info.get(1)) # abc

## what if value does not present in the dictionary.
## get is more effective
print("value for unknow key => ", contact_info.get(10000)) # None

## i don't want None - but default value
print("value for unknow key => ", contact_info.get(10000, "abcdefgh")) # abcdefgh

#contact_info.pop(1123123) # key Error
print(contact_info)

popped_key = contact_info.pop(1)
print(popped_key) # abc

## string reverse
sentence = "my name is john"
result = ""

print("".join(reversed(sentence))) # nhoj si eman ym

for ch in sentence:
    result = ch + result

print(result) # nhoj si eman ym

print(sentence[::-1]) # nhoj si eman ym

