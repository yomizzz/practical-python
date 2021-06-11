# mortgage.py
#
# Exercise 1.7, 1.8, 1.9, 1.10, 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
month = 0

while principal > 0:
    if extra_payment_start_month <=month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        month += 1
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        month += 1
    if principal < 0:
        principal = 0
    print(month, round(total_paid, 2), round(principal, 2)) 


print('Total paid', round(total_paid, 2))
print('Months', month)
