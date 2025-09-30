## solution 

# Python code​​​​​​‌‌‌​​‌​​‌‌​​‌‌​​​​‌​​​‌‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = True
from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        super().__init__()
        self.price = price

    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, company_name):
        self.company_name = company_name
        self.ticker = ticker
        super().__init__(price)

    def get_description(self):
       return f"{self.ticker}: {self.company_name} -- ${self.price}" 

class Bond(Asset):
    def __init__(self, bondprice, bondname, duration, interest):
        super().__init__(bondprice)
        self.bondname = bondname
        self.duration = duration
        self.interest = interest

    def get_description(self):
        return f"{self.bondname}: {self.duration} : ${self.price} : {self.interest}%"


# -------------------------------------------------------------------------
## input

# This is how your code will be called.
# DO NOT change the variable names. You CAN try different values.
ticker = "MSFT"
price = 400.00
description = "Microsoft Corporation"
bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38

# ******* DO NOT CHANGE THIS CODE ********
stock = Answer.Stock(ticker, price, description)
stock_description = stock.get_description()

bond = Answer.Bond(bondprice, bondname, duration, interest)
bond_description = bond.get_description()