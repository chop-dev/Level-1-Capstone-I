import math 

# Request the user the type of interest calculator he will need 
userCalculator = input('''
Choose either 'investment' or 'bond' from the menu below to proceed:
investment  - to calculate the amount of interest you'll earn on interest
bond        - to calculate the amount you'll have to pay on a home loan
''').lower()

# Determine the type of calculator the user picked
if userCalculator == "investment": 
    userAmount = float(input("Enter the amount of money you are depositting: "))
    userRate = float(input("Enter the interest rate you want: "))
    userTime = int(input("How many years are you planning to invelost in: "))
    interestType = input("Do you want 'simple' or 'compound' interest: ").lower()
    
    # Determine the type of interest the user picked 
    if interestType == "simple":        
        interest = round((userAmount * (1 + (userRate/100) * userTime)), 2) # simple interest calculation
        print(f"Your {interestType} interest investment of {userTime} years will pay out R{interest}")
    elif interestType == "compound":    
        interest = round((userAmount * math.pow((1 + userRate), userTime)), 2)  # compound interest calculation
        print(f"Your {interestType} interest investment of {userTime} years will pay out R{interest}")

elif userCalculator == "bond": 
    userAmount = float(input("Enter the present value of the house: "))
    userRate = float(input("Enter the interest rate: ")) / 100
    userTime = int(input("Enter the number of months you plan to repay the bond: "))
    bond = round((userRate  * userAmount) / (1 - math.pow((1 + userRate), (-userTime))), 2) # bond payment calculation
    print(f"Your house with the present value of R{userAmount} is going to take {userTime} payments of R{bond} to be paid off.")
else:
    print("Please choose something from the menu.") # Error Message