colors = ["red", "yellow", "green", "blue", "brown", "black"]

print(colors[0]) # red
## first 3 items
print(colors[:3]) # ['red', 'yellow', 'green']
## last 3 items 
print(colors[-3:]) # ['blue', 'brown', 'black']

## end is exclusive
## slicing for a range
print(colors[1:3]) # ['yellow', 'green']s
print(colors[2:4]) # ['green', 'blue']
print(colors[2:6]) # ['green', 'blue', 'brown', 'black']

# colors.pop(12344) #exception:  pop index out of range

## it needs an index
colors.pop(0)
print(colors) # ['yellow', 'green', 'blue', 'brown', 'black']

## if you know, which item to remove
colors.remove('blue')
print(colors) # ['yellow', 'green', 'brown', 'black']

