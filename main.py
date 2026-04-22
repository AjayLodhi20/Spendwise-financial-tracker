import random
CATEGORIES = ('Food', 'Transport', 'Entertainment', 'Utilities', 'Misc')
# create accounts separate for all
numbers = '1234567890'
numbers = list(numbers)
ACCOUNTS = {}

def account_no(acc_name):
    if acc_name not in ACCOUNTS:
         ACCOUNTS[acc_name] = acc_name.upper() + "".join(random.sample("0123456789",10))
    return ACCOUNTS[acc_name]



account_no('satyam')

print(ACCOUNTS)

# show some info when i write the account name..like account no. name date of account open
# store all user data in a dictionary form
# check if the user has put one of the existing name correctly
# use regex to filter and search
# check if the amount is correctly written
