import math
import argparse

def diff():
    global args
    p = float(args.principal)
    n = int(args.periods)
    interest = float(args.interest)
    i = interest / (12 * 100)
    count = 0
    for m in range(1, n + 1):
        d = (p / n) + (i * (p - ((p * (m - 1)) / n)))
        count += math.ceil(d - (p / n))
        print(f'Month {m}: paid out {math.ceil(d)}')
    print(f'\nOverpayment = {math.ceil(count)}')

def monthly_payments():
    global args
    loan = float(args.principal)
    month = int(args.periods)
    interest = float(args.interest)
    i = interest / (12 * 100)
    monthpay = loan * ((i * math.pow(1 + i, month)) / (math.pow(1 + i, month) - 1))
    print("Your annuity payment = " + str(math.ceil(monthpay)) + "!")
    print("Overpayment = " + str(int(((math.ceil(monthpay) * month) - loan))))

def credit_principal():
    global args
    monthpay = float(args.payment)
    month = int(args.periods)
    interest = float(args.interest)
    i = interest / (12 * 100)
    loan = monthpay / ((i * math.pow(1 + i, month)) / (math.pow(1 + i, month) - 1))
    print("Your loan principal = " + str(int(loan)) + "!")
    print("Overpayment = " + str(int(math.ceil(((math.ceil(monthpay) * month) - loan)))))

def count_months():
    global args
    loan = float(args.principal)
    monthpay = float(args.payment)
    interest = float(args.interest)
    i = interest / (12 * 100)
    n = math.ceil(math.log((monthpay / (monthpay - (i * loan))), 1 + i))
    if n < 12:
        if n == 1:
            print(f"It will take {n} month to repay this loan!")
        else:
            print(f"It will take {n} months to repay this loan!")
    elif n > 12:
        years = math.floor(n / 12)
        month = n % 12
        if month == 0:
            print(f"It will take {years} years to repay this loan!")
        elif month == 1:
            print(f"It will take {years} years and {month} month to repay this loan!")
        else:
            print(f"It will take {years} years and {month} months to repay this loan!")
    print("Overpayment = " + str(int(math.ceil(((math.ceil(monthpay) * n) - loan)))))

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
args = parser.parse_args()

if args.interest is None:
    print("Incorrect parameters.")
    exit()

if args.type == "diff":
    diff()

elif args.type == "annuity":
    if args.payment is None:
        monthly_payments()
    elif args.principal is None:
        credit_principal()
    elif args.periods is None:
        count_months()
else:
    print("Incorrect parameters.")
