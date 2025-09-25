import utils
# from utils import sort_list

utilities = utils.Utility()
print(dir(utilities))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', 
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 
# 'convert_string_to_lower', 'convert_string_to_upper', 'find_num_with_max_freq', 'get_second_highest_number', 
# 'print_logs', 'sort_list']

utilities.convert_string_to_lower("Hello") # hello
second_highest_num = utilities.get_second_highest_number([32,234,56,78,9,43,78,9,543,5,78,55,45656,78,4,67,434])
print(second_highest_num) #543

utilities.find_num_with_max_freq([32,234,56,78,9,43,78,9,543,5,78,55,45656,78,4,67,434]) # num : 78, freq : 4