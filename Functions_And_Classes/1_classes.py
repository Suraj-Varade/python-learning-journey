# the most basic class

class Basic:
    pass    # not doing anything

basic = Basic() # creating an instance

# for methods in dir(basic):
#    print(methods)

class Dog:
    is_animal = bool(1)
    def bark(self):
        print("woof!")

dog = Dog()
dog.bark() # woof! 

## if we missed to add self in the method then -> TypeError: Dog.bark() takes 0 positional arguments but 1 was given

## you can create as many instances of this class as you need
rufus = Dog()
dog.bark() # woof!  

## watch out for class attributes that can change "state" from every instance and objects
dog.is_animal = False
print(f"is dog an animal ? {dog.is_animal}") # False 
print(f"is rufus an animal ? {rufus.is_animal}") # True

rufus = dog
print(f"is dog an animal ? {dog.is_animal}") # False 
print(f"is rufus an animal ? {rufus.is_animal}") # False

sparky = Dog()
sparky.bark()
print(f"is sparky an animal ? {sparky.is_animal}") # True

## self ->> you must create a methods with 'self' always.

class Person:
    name = "xxxx"
    address = "xxxx"

    def print_info(self, name, address):
        if not name:
            name = self.name
        if not address:
            address = self.address
        print(name, address)

adam = Person()
adam.print_info("adam", "LA") # adam LA
adam.print_info("", "") # xxxx xxxx
