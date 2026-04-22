import random
CATEGORIES = ('Food', 'Transport', 'Entertainment', 'Utilities', 'Misc')
# create accounts separate for all
numbers = '1234567890'
numbers = list(numbers)

def account_no():
    account_holder ={}
    while True:
        acc_name = input("enter account name").upper()
        if acc_name != str:
            print("Name should not include no. or symbol or lowercase")
            continue
        random.shuffle(numbers)
        new_numbers = "".join(numbers)
        account_holder[acc_name] = f"{acc_name}{new_numbers}"
account_no('satyam')
print(account_holder)

# show some info when i write the account name..like account no. name date of account open
# store all user data in a dictionary form
# check if the user has put one of the existing name correctly
# use regex to filter and search
# check if the amount is correctly written
