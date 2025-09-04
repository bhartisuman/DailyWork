total_price = float(input('Please enter the total price pf product: '))
down_payment = float(input('Please enter the down payment: '))
loan_period = int(input('Please enter the loan period in months: '))
interest_rate = float(input('Please enter the monthly interest rate: '))
loan_amount = total_price - down_payment
emi = loan_amount * interest_rate *((1+interest_rate)**loan_period)/(((1+interest_rate)**loan_period)-1)
print(f'The total monthly emi is: {emi}')
print(f'The total interest paid is: {(emi*loan_period)-loan_amount}')