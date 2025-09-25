## if condition
condition = True
if condition:
    print("condition is True") # ondition is True
else:
    print("condition is False")

print("---------------------------------------------------------")

groceries = []
if groceries:
    print("we have some groceries !!!")
else:
    print("no groceries found") # no groceries found

print("---------------------------------------------------------")

invites = ["john", "steve"]
if invites:
    print("we have some invities!!") # we have some invities!!
else:
    print("no invities!!")

print("---------------------------------------------------------")    

properties = 0
if properties:
    print("we have properties.")
else:
    print("no properties found.") # no properties found.

print("---------------------------------------------------------")   

benefits = None
if benefits:
    print("we have some benefits!!!")
elif benefits == None:
    print("no benefits") # no benefits

print("---------------------------------------------------------") 

## Negative conditions

name = None
if name:
    print(f"name is valid : {name}")
elif not name:
    print("name is invalid : None")
else:
    print("no condition match")

print("---------------------------------------------------------") 

married = bool(1)
has_kids = False

if married and has_kids:
    print("person is maried and has kids")
elif married and not has_kids:
    print("person is married but has no kids")
else:
    print("person is not married")

print("---------------------------------------------------------") 

