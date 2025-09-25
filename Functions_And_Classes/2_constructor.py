# the constructor in python is with the special method called __init__ (double underscore/Dunder method) 
class Employee:
    def __init__(self, id, name, address, mobile):
        self.id = id
        self.name = name 
        self.address = address
        self.mobile = mobile
    
    def print_info(self):
        print(self.id, self.name, self.address, self.mobile)

    def print_country(self, mobile):
        if not mobile:
            mobile = self.mobile
        first_2_characters = mobile[:2]
        if first_2_characters == "91":
            print(f"country is india.")
        else:
            print("outside india.")

permanent_employee = Employee(1, "john", "Mumbai", "91904536272")
permanent_employee.print_info()
permanent_employee.print_country("91904536272")

