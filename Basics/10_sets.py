## they look like dict, lists.
## they allow us to keep unique items.
# they are un-ordered
unique = set()
print(unique) # set()
print(type(unique)) # <class 'set'>

unique.add('one')
unique.add('two')
unique.add('three')
unique.add('four')

for item in unique:
    print(item)

print(unique) # {'three', 'one', 'two', 'four'}
# unique.pop()
print(unique) # {'one', 'two', 'four'}

## check if item exists in the set
itemBeingSearched = 'four'
if 'four' in unique:
    print(f'item found in a set') # item found in a set
else:
    print('item no found')
