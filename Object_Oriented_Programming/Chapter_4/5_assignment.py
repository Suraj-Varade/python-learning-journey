# Python code​​​​​​‌‌‌​​‌​​‌‌​​‌‌‌‌‌​‌‌‌‌‌​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

from dataclasses import dataclass

@dataclass ## if you want your own eq implementations - then @dataclass(eq = False)
class Asset():
    price: float

    def __gt__(self, value):
        return self.price > value.price
        
    def __lt__(self, value):
        return self.price < value.price

    def __ge__(self, value):
        return self.price >= value.price
        
    def __le__(self, value):
        return self.price <= value.price

@dataclass
class Stock(Asset):
    price: float
    ticker: str
    company: str
    
@dataclass
class Bond(Asset):
        price: float
        description : str
        duration : int
        interest : float

# ----------------------------------------------------------------------
## inputs : 

# This is how your code will be called.
# DO NOT change the variable names. You CAN try different values.
ticker = "ABCD"
price = 200.00
description = "ABCD Corporation"

bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38

# ******* DO NOT CHANGE THIS CODE ********
stock = Answer.Stock(price, ticker, description)
bond = Answer.Bond(bondprice, bondname, duration, interest)

is_eq = (stock == bond)
is_gt = (stock > bond)
is_lt = (stock < bond)
is_gte = (stock >= bond)
is_lte = (stock <= bond)