readonly_items = ('first', 'second', 'third', 4)
print(readonly_items) # ('first', 'second', 'third', 4)
print(type(readonly_items)) # <class 'tuple'>

for item in readonly_items:
    print(item)
'''
first
second
third
4
'''
print(f"find index of item in the tuple : {readonly_items.index('first')}") # 0
print(f"find index of item in the tuple : {readonly_items.index(4)}") # 3

# find out all the available methods in tuple
for method in dir(tuple):
    if method.startswith('_'):
        continue
    print(method)
'''
count
index
'''
for method in dir(tuple):
    print(method)
## all the methods started with __ are dunder methods (double underscore)
## They are special methods that python uses internally to make objects behave in certain ways.
## you usually don't call them directly - instead, python calls them for you when you use 
## operators or built-ins 
t = (1,2,3)
print(len(t)) # -- behind the scene => calls t.__len__()