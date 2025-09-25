class Budget:
    def __init__(self, budget):
        self.budget = budget
        self.print_logs(f"total budget allocated for this scheme : {self.budget}")

    def add_expense(self, amount):
        if self.budget < amount:
            self.print_logs(f"this operation not allowed, your amount is exceeding the budget.")
            return

        self.budget = self.budget - amount
        self.print_logs(f"budget left : {self.budget}")
    
    def add_budget(self, new_budget_amount):
        self.budget += new_budget_amount
        self.print_logs(f"new budget amount : {self.budget}")

    def print_logs(self, message):
        print(message)
        

event = Budget(10000) # total budget allocated for this scheme : 10000
event.add_expense(11000) # this operation not allowed, your amount is exceeding the budget.
event.add_budget(10000) # new budget amount : 20000
event.add_expense(11000) # budget left : 9000
print(f"current budget : {event.budget}") # 9000

