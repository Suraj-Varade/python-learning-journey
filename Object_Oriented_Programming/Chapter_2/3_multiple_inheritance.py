class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"

class C(A, B):
    def __init__(self):
        super().__init__()


c = C()
print(c.prop1)
print(c.prop2)
'''
prop1
prop2
'''

# ----------------------------------------------------------------------------------
print("----------------------------------------------------------------------------------")
## what if both the classes have same property.

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"

class C(A, B):
    def __init__(self):
        super().__init__()
    
    def show_properties(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)


c = C()
c.show_properties()
'''
prop1
prop2
Class A
'''
## -- method resolution order, class c doesn't have the property "name", hence interpreter 
# looks from left to right, since class C(A, B) -->> it finds A first hence, the property from class A
# will invoke.

print(C.__mro__) 
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
