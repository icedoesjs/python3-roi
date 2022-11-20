import os
clear = lambda: os.system('cls')
from time import sleep
from collections import Counter
clear()
    

class roi_calc():
    def __init__(self, p_cost = 50, r_cost = 50, units = 1, monthly_expenses = []):
        self.self = self
        self.p_cost = p_cost
        self.r_cost = r_cost
        self.units = units
        self.expenses = monthly_expenses
        
    def validate_number(self, num):
        if not num.isnumeric():
            return False
        else:
            return True
        
    def invalid_input(message):
        clear()
        print(message)
        sleep(3)
    
    # Set property cost
    def set_beginning_costs(self, p_cost, r_cost, units):
        self.p_cost = p_cost
        self.r_cost = r_cost 
        self.units = units
    
roi_calc = roi_calc()
expenses = {}

def gather_expenses():
    run = True
    clear()
    while run:
        clear()
        exp = input("Provide a monthly expense name followed by a colon and the expense value, Do not include mortgage. (Ex: Power:50, Repairs: 100)\nOnce all expenses are provided input END\n\n")
        if exp.lower() == "end" or exp.lower() == "quit":
            run = False
        elif not ":" in exp:
            clear()
            print("No colon was provided.")
            sleep(3)
        else:
            e_name = exp.split(":")[0]
            e_cost = exp.split(":")[1]
            if e_name.lower() in expenses:
                clear()
                print("That expense was already provided.")
                sleep(3)
            else:
                expenses[e_name.lower()] = int(e_cost)
                

while True:
    clear()
    # Get property cost
    p_cost = input("How much is the property? (Do NOT provide a $)\n\n")
    if roi_calc.validate_number(p_cost):
        clear()
        # Get rental cost per unit
        r_cost = input("How much are you charging for rent per unit? (Do not provide a $)\n\n")
        if roi_calc.validate_number(r_cost):
            clear()
            # Get total amount of units
            units = input("How many units will you be renting out?\n\n")
            if roi_calc.validate_number(units):
                gather_expenses() # Add all property expenses (while loop)
                clear()
                mortgage = input("How much is the monthly mortage? (Do not provide a $)\n\n")
                if roi_calc.validate_number(mortgage):
                    month_exp = sum(expenses.values())
                    income = int(r_cost) * int(units) ## Monthly cash flow 
                    monthly_income = int(income) - int(month_exp) # Get monthly income by taking your income and taking away monthly expenses
                    clear()
                    int_inv = input("How much is the intial investment you are going to make (downpayment, closing costs etc)? (Do not provide a $)\n\n")
                    if roi_calc.validate_number(int_inv):
                        clear()
                        yearly_income = monthly_income * 12 # Yearly income
                        ret_percentage = yearly_income / int(int_inv) 
                        print(f"Your return percentage will be {ret_percentage}%")
                        sleep(7)
                        break
                    else:
                        roi_calc.invalid_input("The downpayment amount was invalid.")
                else:
                    roi_calc.invalid_input("The property cost provided was invalid.")
            else:
                roi_calc.invalid_input("The amount of units provided was invalid.")
        else:
            roi_calc.invalid_input("The rental cost provided was invalid.")
        
    else:
        roi_calc.invalid_input("The property cost you provided was invalid.")