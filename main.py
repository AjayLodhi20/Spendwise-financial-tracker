import random
CATEGORIES = ('Food', 'Transport', 'Entertainment', 'Utilities', 'Misc')
# create accounts separate for all
numbers = '1234567890'
numbers = list(numbers)

def account_no(acc_name):
    acc_holder= {}
    if isinstance(acc_name, str):
        acc_name = acc_name.upper()
        random.shuffle(numbers)
        new_list = "".join(numbers)
        acc = f"{acc_name}{new_list}"
        return acc_holder[acc_name]
    else:
        raise AttributeError("write string in the function call..")

print(account_no('satyam'))

# show some info when i write the account name..like account no. name date of account open
# store all user data in a dictionary form
# check if the user has put one of the existing name correctly
# use regex to filter and search
# check if the amount is correctly written
