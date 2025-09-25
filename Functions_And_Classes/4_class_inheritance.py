class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name 
        self.print_logs(f"employee created : id - {self.id}, name - {self.name}")

    def print_logs(self, message):
        print(f"{message}")

## inheritance - Employee ->>>>> PermanentEmployee
class PermanentEmployee(Employee):
    def __init__(self, id, name, pay):
        super().__init__(id, name)
        self.monthly_pay = pay
        self.print_logs(f"permanent employee monthly pay : {self.monthly_pay}")


## inheritance - Employee ->>>>> TemporaryEmployee
class TemporaryEmployee(Employee):
    def __init__(self, id, name, pay):
        super().__init__(id, name)
        self.hourly_pay = pay
        self.print_logs(f"temporary employee hourly pay : {self.hourly_pay}")
    

# employee = Employee(1, "john")
permanent_employee = PermanentEmployee(2, "kent", 345000)
# employee class : id - 2, name - kent
# permanent employee monthly pay : 345000

temporary_employee = TemporaryEmployee(3, "Bob", 500)
# employee class : id - 3, name - Bob
# temperory employee hourly pay : 500
