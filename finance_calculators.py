# This Python program allows user to access two different financial calculators:
# an investment calculator, and a home loan repayment calculator.
# the users can choose the type of financial calculation they want to do
# the program ask usern for input based on the type of calculation they want to perform
# the program then performs some mathematical operations on the input and displays the 
# output to the user

import math

# user manual
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("investment \t - to calculate the amount of interest you'll earn on a capital invested")
print("bond \t - to calculate the amount you'll have to pay on a home loan")

# input from user
calculation_type = input("investment / bond: ").lower()

# amount = 1 #initialise amount

# investment calculation
if calculation_type == "investment":
    principal = float(input("Enter the amount you want to invest: "))
    inv_rate = float(input("Enter the rate (e.g., 8, 9, 10, ...): ")) * 0.01
    inv_duration = int(input("Enter the number of years to invest for: "))
    interest_type = input("Enter the interest type (simple / compound): ").lower()

    # interest calculations
    # amount using simple interest calculation
    if interest_type == "simple":
        inv_amount =  principal * (1 + inv_rate * inv_duration)
        print("Interest type: {}\t Amount: {:.2f}".format(interest_type, inv_amount))

    # amount using compound interest calculation
    elif interest_type == "compound":
        inv_amount = principal * math.pow((1 + inv_rate), inv_duration)
        print("Interest type: {}\t Amount: {:.2f}".format(interest_type, inv_amount))
    # invalid entry from user
    else:
        print("Invalid interest type.")

# bond calculation
elif calculation_type == "bond":
    house_value = float(input("Enter the current value of the house (e.g., 100000): "))
    bond_rate = float(input("Enter the rate (e.g., 8, 9, 10, ...): ")) * 0.01
    bond_duration = int(input("Enter the number of months to repay the bond (e.g., 120): "))

    bond_amount = (bond_rate * house_value) / (1 - math.pow((1 + bond_rate), (-bond_duration)))
    print("Monthly repayment: {:.2f}".format(bond_amount))

# invalid input from user
else:
    print("This option is not available for standard user. Upgrade to premium user.")




