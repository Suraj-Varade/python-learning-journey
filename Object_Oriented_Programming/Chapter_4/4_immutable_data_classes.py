from dataclasses import dataclass

## immutable data classes.

@dataclass
class ImmutableClass: # "frozen" parameter makes the class immutable
    value1 : str = "Value 1"
    value2 : int = 0

obj = ImmutableClass()
print(obj.value1) # Value 1

obj.value1 = "new updated value 1"
print(obj.value1) # new updated value 1

# ----------------------------------------------------------------------------------
## what if i don't want to allow updates.
# setting frozen attribute to True.
@dataclass(frozen=True)
class ImmutableClass: # "frozen" parameter makes the class immutable
    value1 : str = "Value 1"
    value2 : int = 0

obj = ImmutableClass()
print(obj.value1) # Value 1

obj.value1 = "new updated value 1"
print(obj.value1) # new updated value 1
'''
Traceback (most recent call last):
  File "/Users/surajvarade/Personal/Programs/Python/Object_Oriented_Programming/Chapter_4/4_immutable_data_classes.py", line 27, in <module>
    obj.value1 = "new updated value 1"
    ^^^^^^^^^^
  File "<string>", line 16, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'value1'
'''