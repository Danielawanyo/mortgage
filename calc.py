def mortgage_calculator():
    loan_amount = float(input("Enter the loan amount: GHS "))
    interest_rate = float(input("Enter the interest rate: "))
    term_of_loan = int(input("Enter the term of the loan in years: "))

    monthly_interest_rate = interest_rate / 100 / 12
    number_of_monthly_payments = term_of_loan * 12
    
    mortgage = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_monthly_payments  / ((1 + monthly_interest_rate) ** number_of_monthly_payments - 1)
    
    print('The monthly mortgage payment is: GHS' , round(mortgage, 2))



mortgage_calculator()