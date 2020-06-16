'''credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
print(credit_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)'''


"""def count_of_month(cred):
    time_for_credit = cred / monthly_pay
    if time_for_credit > round(time_for_credit):
        time_for_credit = round(time_for_credit) + 1
        print(f'It takes {int(time_for_credit)} months to repay the credit')
    else:
        time_for_credit = round(time_for_credit)
        if time_for_credit == 1:
            print(f'It takes {int(time_for_credit)} month to repay the credit')
        else:
            print(f'It takes {int(time_for_credit)} months to repay the credit')


def pay_of_month(cred):
    if cred % count_month == 0:
        month_payment = cred / count_month
        print(f'Your monthly payment = {int(month_payment)}')
    else:
        month_payment = cred / count_month
        if month_payment > round(month_payment):
            month_payment = round(month_payment) + 1
        else:
            month_payment = round(month_payment)
        last_month_pay = cred - month_payment * (count_month - 1)
        print(f'Your monthly payment = {month_payment} with last month payment = {last_month_pay}.')


credit = int(input('Enter the credit principal:\n> '))
choose_calculation = input('What do you want to calculate?\n'
                           'type "m" - for count of months,\n'
                           'type "p" - for monthly payment:\n> ')
if choose_calculation == 'm':
    monthly_pay = int(input('Enter monthly payment:\n> '))
    count_of_month(credit)
elif choose_calculation == 'p':
    count_month = int(input('Enter count of months:\n> '))
    pay_of_month(credit)
"""
"""import math


def count_of_month():
    credit_principal = int(input('Enter credit principal:\n> '))
    monthly_pay = int(input('Enter monthly payment:\n> '))
    credit_interest = float(input('Enter credit interest:\n> '))
    i = credit_interest / 1200
    n = math.log((monthly_pay / (monthly_pay - i * credit_principal)), (i + 1))
    n = math.ceil(n)
    years = n // 12
    month = n - years * 12
    if years and month > 0:
        print(f'You need {years} years and {month} months to repay this credit!')
    elif years > 0 and month == 0:
        print(f'You need {years} years to repay this credit!')
    elif years == 0 and month > 0:
        print(f'You need {month} years to repay this credit!')


def annuity_payment():
    credit_principal = int(input('Enter credit principal:\n> '))
    periods = int(input('Enter count of periods:\n> '))
    credit_interest = float(input('Enter credit interest:\n> '))
    i = credit_interest / 1200
    annuity = math.ceil((credit_principal * (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))))
    print(f'Your annuity payment = {annuity}!')


def credit_pr():
    monthly_pay = float(input('Enter monthly payment:\n> '))
    periods = int(input('Enter count of periods:\n> '))
    credit_interest = float(input('Enter credit interest:\n> '))
    i = credit_interest / 1200
    credit_principal = monthly_pay / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))
    print(f'Your credit principal = {round(credit_principal)}!')


choose_calculation = input('What do you want to calculate?\n'
                           'type "n" - for count of months,\n'
                           'type "a" - for annuity monthly payment,\n'
                           'type "p" - for monthly payment:\n> ')
if choose_calculation == 'n':
    count_of_month()
elif choose_calculation == 'a':
    annuity_payment()
elif choose_calculation == 'p':
    credit_pr()"""

import math
import sys


def diff(pr, per, cred):
    credit_principal = pr
    periods = per
    credit_interest = cred
    i = credit_interest / 1200
    m = 1
    d_sum = 0
    while m <= periods:
        d = credit_principal / periods + i * (credit_principal - ((credit_principal * (m - 1)) / periods))
        d_sum += math.ceil(d)
        print(f'Month {m} : paid out {math.ceil(d)}')
        m += 1
    overpay = d_sum - credit_principal
    print(f'\nOverpayment = {round(overpay)}')


def count_of_month(pr, month_p, cred):
    credit_principal = pr
    monthly_pay = month_p
    credit_interest = cred
    i = credit_interest / 1200
    n = math.log((monthly_pay / (monthly_pay - i * credit_principal)), (i + 1))
    n = math.ceil(n)
    years = n // 12
    month = n - years * 12
    pay_sum = n * monthly_pay
    overpay = pay_sum - credit_principal
    if years > 0 and month > 0:
        print(f'You need {years} years and {month} months to repay this credit!')
    elif years > 0 and month == 0:
        print(f'You need {years} years to repay this credit!')
    elif years == 0 and month > 0:
        print(f'You need {month} years to repay this credit!')
    print(f'\nOverpayment = {overpay}')


def annuity_payment(pr, per, cred):
    credit_principal = pr
    periods = per
    credit_interest = cred
    i = credit_interest / 1200
    annuity = math.ceil((credit_principal * (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))))
    pay_sum = annuity * periods
    overpay = pay_sum - credit_principal
    print(f'Your annuity payment = {annuity}!')
    print(f'\nOverpayment = {overpay}')


def credit_pr(month_p, per, inter):
    monthly_pay = month_p
    periods = per
    credit_interest = inter
    i = credit_interest / 1200
    credit_principal = monthly_pay / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))
    print(f'Your credit principal = {round(credit_principal)}!')
    pay_sum = monthly_pay * periods
    overpay = credit_principal - pay_sum
    print(f'\nOverpayment = {overpay}')


argv = sys.argv
param = []
for item in argv:
    param.append(item.split('='))
# verification
if len(param) == 5 and int(param[2][1]) > 0 and int(param[3][1]) > 0 and float(param[4][1]) > 0:
    if param[1][1] == 'diff':
        diff(int(param[2][1]), int(param[3][1]), float(param[4][1]))
    elif param[1][1] == 'annuity':
        if param[2][0][2:] == 'principal' and param[3][0][2:] == 'periods' and param[4][0][2:] == 'interest':
            annuity_payment(int(param[2][1]), int(param[3][1]), float(param[4][1]))
        elif param[2][0][2:] == 'payment' and param[3][0][2:] == 'periods' and param[4][0][2:] == 'interest':
            credit_pr(int(param[2][1]), int(param[3][1]), float(param[4][1]))
        elif param[2][0][2:] == 'principal' and param[3][0][2:] == 'payment' and param[4][0][2:] == 'interest':
            count_of_month(int(param[2][1]), int(param[3][1]), float(param[4][1]))
else:
    print('Incorrect parameters')
# ver2
"""import math
import argparse
import sys
parser = argparse.ArgumentParser(description='Calculate credit details')
parser.add_argument('--type', type=str, help='Determines type of payments')
parser.add_argument('--principal', type=int, help='Principal of credit')
parser.add_argument('--payment', type=int, help='Value of payment')
parser.add_argument('--interest', type=float, help='Credit interest')
parser.add_argument('--periods', type=int, help='Number of periods')
args = parser.parse_args()
argm = sys.argv

def diff_month_payment(type, principal, periods,interest):
    i  = args.interest / 1200
    ind = 1
    overpayment = 0
    while ind <= args.periods:
        D = args.principal / args.periods + i * (args.principal - (args.principal * (ind - 1) / args.periods))
        print('Month ' + str(ind) + ': paid out ' + str(math.ceil(D)))
        ind = ind + 1
        overpayment += math.ceil(D)
    statement = ("\nOverpayment = " + str(overpayment - principal))
    return statement

def annuity_payment(type, pricnipal, periods, interest):
    i = args.interest / 1200
    ann_payment = (args.principal * i * (1 + i)**args.periods) /((1 + i)**args.periods - 1)
    overpayment_2 = math.ceil(ann_payment) * args.periods - args.principal
    print("Yout annuity payment = " + str(math.ceil(ann_payment)) + "!")
    statement_2 = ("Overpayment = " + str(overpayment_2))
    return statement_2
def principal_calc(type, payment, periods, interest):
    i = args.interest / 1200
    credit_principal = args.payment / ((i * (1 + i)**args.periods)/((1 + i)**args.periods-1))
    print("Your credit principal = " + str(math.floor(credit_principal)) +"!")
    overpayment_3 = ("Overpayment = " + str(args.payment * args.periods - math.floor(credit_principal)))
    return overpayment_3

def how_many_months(type, principal, payment, interest):
    i = args.interest / 1200
    number_of_months = math.log((args.payment)/(args.payment - i * args.principal), (1 + i))
    months_rounded = math.ceil(number_of_months)
    if months_rounded % 12 == 0:
        x = months_rounded / 12
        print("You need ", int(x), "years to repay this credit!")
    elif months_rounded < 12:
        print("You need ", months_rounded, "months to repay this credit!")
    else:
        years = months_rounded // 12
        months = months_rounded % 12
        print("You need ", years, "years and ", months, "months to repay this credit!")
    return("Overpayment = " + str(math.ceil(months_rounded * args.payment - args.principal)))


if len(sys.argv) != 5:
    print("Incorrect parameters")
elif args.type == "diff" and not args.payment:
    print(diff_month_payment(args.type, args.principal, args.periods, args.interest))
elif args.type == "annuity" and not args.payment:
    print(annuity_payment(args.type, args.principal, args. periods, args.principal))
elif args.type == "annuity" and not args.principal:
    print(principal_calc(args.type, args.payment, args.periods, args.interest))
elif args.type == "annuity" and not args.periods:
    print(how_many_months(args.type, args.principal, args.payment, args.interest))
else:
    print("Incorrect parameters")"""

# ver3
"""import math
import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="Credit Calculator Project")

# Add the parameters positional/optional

parser.add_argument('--type', help = "Type of Payment (Annuity or Differential")
parser.add_argument('--payment', help = "Monthly payment", type = int)
parser.add_argument('--principal', help = "Credit principal", type = int)
parser.add_argument('--periods', help = "Count of months", type = int)
parser.add_argument('--interest', help = "Credit interest (rate of interest)", type = float)

# Parse the arguments
args = parser.parse_args()

if args.type not in ['annuity', 'diff']:
    print('Incorrect Parameters')
    exit(0)

if args.type == 'diff' and args.payment != None:
    print('Incorrect Parameters')
    exit(0)

args_list = [args.type, args.payment, args.principal, args.periods, args.interest]
# print(args_list)

count = 0
for item in args_list:
    if item == None:
        count += 1

if count > 1:
    print('Incorrect Parameters')
    exit(0)

if args_list[1] != None and args_list[1] < 0 or args_list[2] != None and args_list[2] < 0 or args_list[3] != None and args_list[3] < 0 or args_list[4] != None and args_list[4] < 0.0:
    print('Incorrect Parameters')
    exit(0)


if args.type == 'annuity' and args.payment != None and args.principal != None and args.interest != None:

    nominal_interest = args.interest / (12 * 100)

    months = math.ceil(math.log (args.payment
                                 / (args.payment - nominal_interest * args.principal), (1 + nominal_interest)))

    overpayment = months * args.payment - args.principal

    year = months // 12
    months = months % 12

    if months == 0:
        print('You need', year, 'years to repay this credit!')
    elif year == 0:
        print('You need', months, 'months to repay this credit!')
    else:
        print('You need', year, 'years and', months, 'months to repay this credit!')
    print('Overpayment = ', overpayment)


elif args.type == 'annuity' and args.periods != None and args.payment != None and args.interest != None:

    nominal_interest = args.interest / (12 * 100)

    complex_value = (nominal_interest * math.pow(1 + nominal_interest, args.periods)) / (math.pow(1 + nominal_interest, args.periods) - 1)
    credit_principal = int(args.payment / complex_value)

    overpayment = args.periods * args.payment - credit_principal

    print('Your credit principal =', str(credit_principal) + '!')
    print('Overpayment = ', overpayment)

elif args.type == 'annuity' and args.periods != None and args.principal != None and args.interest != None:

    nominal_interest = args.interest / (12 * 100)

    complex_value = (nominal_interest * math.pow(1 + nominal_interest, args.periods)) / (math.pow(1 + nominal_interest, args.periods) - 1)

    monthly_payment = math.ceil(args.principal * complex_value)
    overpayment = args.periods * monthly_payment - args.principal

    print(('Your annuity payment = {}!').format(monthly_payment))
    print('Overpayment = ', overpayment)

elif args.type == 'diff' and args.periods != None and args.principal != None and args.interest != None:
    nominal_interest = args.interest / (12 * 100)
    diff_total_amount = 0
    for i in range(1, args.periods+1):
        diff_amount = math.ceil(args.principal/args.periods + nominal_interest * args.principal * (1 - (i -1) / args.periods))
        diff_total_amount += diff_amount
        print(('Month {}: paid out {}').format(i, diff_amount))
    overpayment = diff_total_amount - args.principal
    print('Overpayment = ', overpayment)
"""