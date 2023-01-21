import math

'''
PSEUDOCODE

print out opening menu statement for user to select from the following:
    'investment - to calculate the amount of interest you'll earn on your investment'
    'bond - to calculate the amount you'll have to pay on a home loan'
ensure all user inputs here are transformed to lowercase

set up if/elif/else statements for the following:

    if user selects 'investment':
        create user input variables for the following:
            deposit - float
            interest rate - float
            no of years investing - int
        create another variable labelled as 'interest'
        store user input for the question 'would you like simple or compound interest?'
        ensure user input is stored as lowercase
        if user input is 'compound':
            create new float variable to store compound interest formula
            set it equal to:
                deposit * math.pow ((1 + interest rate), no of years)
            print it out to 2 decimal points
        else if user input is 'simple':
            create new float variable to store simple interest formula
            set it equal to:
                deposit * (1 + interest rate * no of years)
            print it out to 2 decimal points
        else, for all invalid user inputs:
            print an error message

    else if user selects 'bond':
        create user input variables for the following:
            present value of house - float
            interest rate - float
            no of months repaying - int
        create new float variable to store bond repayment formula
        set it equal to:
            (monthly interest rate . present value) / (1 - (1 + monthly interest rate) ^ ( - no of months))
        print it out to 2 decimal points]
    
    else, for all invalid user inputs:
        print an error message

'''

print("choose either 'investment' or 'bond from the menu below to proceed:\n")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

menu_choice = input("choice: ").lower()

# for each formula, interest rate has to be divided by 100 in order to be utilised in the function
# saving each of the user input variables as floats except for no_of_yrs which is int
# will round to 2 decimal places at the end when printing final amount using f-string formatting
if menu_choice == "investment":
    deposit = float(input("please enter the amount of money you are depositing: £"))
    interest_rate_inv = float(input("please enter the annual interest rate (no need to include the %): "))
    no_of_yrs = int(input("please enter the total number of years you plan on investing: "))
    interest = input("would you like simple or compound interest?: ").lower()

    # an additional else statement is implemented here to error check for invalid user inputs at this selection
    if interest == "simple":
        simple_interest = float(deposit * (1 + (interest_rate_inv/100) * no_of_yrs))
        print(f"\nthe total amount you will earn on your investment is £{simple_interest:.2f}")
    elif interest == "compound":
        compound_interest = float(deposit * math.pow((1 + (interest_rate_inv/100)), no_of_yrs))
        print(f"\nthe total amount you will earn on your investment is £{compound_interest:.2f}")
    else:
        print("error: please retry answering with either 'simple' or 'compound'")

# here i created an additional variable to store the monthly interest rate by dividing user input by 12
# this was for readability when i wrote out the the bond repayment formula
elif menu_choice == "bond":
    present_house_value = float(input("please enter the present value of the house: £"))
    interest_rate_bond = float(input("please enter the annual interest rate (no need to include the %): "))
    monthly_interest_rate = interest_rate_bond / 12
    no_of_months = int(input("please enter the number of months over which the bond will be repaid: "))
    bond_repayment = float(((monthly_interest_rate / 100) * present_house_value) / (1 - (1 + (monthly_interest_rate / 100)) ** (- no_of_months)))
    print(f"\nthe amount you will have to pay on a home loan each month is £{bond_repayment:.2f}")

else:
    print("sorry - invalid response. please try again and choose either 'investment' or 'bond'.")
