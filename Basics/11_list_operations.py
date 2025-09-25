fruits = []
fruits.append("orange")
fruits.append("apple")

print(fruits) # ['orange', 'apple']

## insert value at specific index
fruits.insert(0, "watermelon")
print(fruits) # ['watermelon', 'orange', 'apple']

## add 2 lists
vegetables = ["cucumber", "carrots"]
mixed = fruits + vegetables
print(mixed) # ['watermelon', 'orange', 'apple', 'cucumber', 'carrots']

mixed.append(["suger", "salt"])
print(mixed) # ['watermelon', 'orange', 'apple', 'cucumber', 'carrots', ['suger', 'salt']]

mixed.extend(["oil", "jaggery"])
print(mixed) # ['watermelon', 'orange', 'apple', 'cucumber', 'carrots', ['suger', 'salt'], 'oil', 'jaggery']