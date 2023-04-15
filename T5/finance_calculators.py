# finance_calculators.py
"""References:
Re. converting float variable to string with 2 decimal places:
https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

I have applied learning from later Tasks and advice from mentor,
so pseudocode is in pseudocode.txt and aiming to follow PEP8/style guides.
No code snippets were copied, but functions are used.
"""


# Import libraries:
import math

# Define functions
# Function to calculate investment interest.
def calc_investment():
    
    # Request inputs for deposit amount, annual interest rate
    principal = float(input ("How much are you depositing? £"))
    time = float(input("How many years do you want to invest for? "))
    
    # User confirms number of years to invest, whether to use compound/simple interest.
    interest_type = input("Do you want to calculate 'simple' or 'compound' interest? ")
    interest = float(input("What is the yearly rate of interest? (Omit the '%') "))
    # Convert % to decimal form for calculation below.
    rate = interest/100
    
    # Use either simple or compound formula to calculate totals at end of investment period:
    if interest_type == "simple":
        amount = principal * (1 + (rate*time) )
    
    elif interest_type == "compound":
        amount =  (principal * math.pow ( (1 + rate ),time))
    
    # Having calculated the total amount, will now subtract the principal to give the interest earned
    extra = (amount - principal)
    # Format extra and principal to 2 decimal places (standard currency format)
    extra = format(extra, ".2f")
    amount = format(amount, ".2f")
    
    # Exit function returning string explaining the interest earned, which is
    # the extra amount gained beyond the original sum invested.
    return (f"£{extra} interest earned on £{principal} initial investment.")

# Function to calculate bond repayments.
def calc_bond():
    # Request input for house value and months to repay:
    house_value = int(input ("Enter the current value of the house, to nearest 1 GBP: £"))
    number_months = int(input("How many months will it take to repay the bond? Enter an integer: "))
    
    # Request annual % interest rate, convert to monthly %, then into decimal.     
    annual_interest = float(input("What is the annual interest rate? (Omit the '%'): "))
    rate = (annual_interest/12)/100    
    
    # Calculate repayment amount:
    result = float((rate * house_value) / (1 - (1 + rate)**(-number_months)))
    # Format repayment to 2 decimal places, following currency conventions.
    repayment = format(result, ".2f")
    
    # exit function with string explaining the repayment amount.
    return (f"£{repayment} is the monthly repayment for a £{house_value} house over {number_months} months.")

# Main program sequence
def run_program():
    
    # User chooses from available program options:
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan")
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    # Convert input to lowercase to avoid impact from capitalisation
    choice = choice.lower()

    # If user enters 'bond', call function to calculate bond repayments and display message to user
    if choice.lower() == "bond":
        # Display result of function to user
        print (calc_bond())
        
    # If user enters 'investment', call function for investment calculation and display message to user
    elif choice == "investment":
        # Display result of function to user
        print(calc_investment())
        
    # If user has not entered one of the options, display an error.
    else:
        print ("Error, input should be 'bond' or 'investment'")

run_program()
# End of program. Thanks for reading.