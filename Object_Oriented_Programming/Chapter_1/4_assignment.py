# Python code​​​​​​‌‌‌​​‌​​‌​‌‌‌​​​‌‌​‌‌‌‌​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Stock:
    def __init__(self, ticker, price, name):
        self.ticker_symbol = ticker
        self.price = price
        self.company_name = name

    def get_description(self):
        return f"{self.ticker_symbol}: {self.company_name} -- ${self.price}"

# ------------------------------------------------------------
## test code

# This is how your code will be called.
# DO NOT change these variable names. You CAN change the values.
ticker = "GOOG"
price = 185.43
company = "Google LLC"

# DO NOT change this code:
symbol = Answer.Stock(ticker, price, company)

description = symbol.get_description()

# --------------------------------------------------------------
## console output
'''
Well done! You reached the expected result.
Your code returned: GOOG: Google LLC -- $185.43
--- -- -- -- -- -- -- -- -- -- -- --
'''