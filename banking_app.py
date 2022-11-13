#pseudo code for banking program
# intro to programming principles part 5, activity 3

# Create a cash machine program that takes a pin number and amount. Outputs cash is being dispensed if the pin is correct and there is enough money to withdraw. Finally outputs the new balance.

# Be creative with your solution! 

import sys, random

#Initializing variables
first_name, last_name, email, address, acc_num, pin, balance = '', '', '', '', '', '', ''

#Initializing dictionary database
database = {
    "scott" : {
        'first_name' : 'Scott',
        'last_name' : 'Evans',
        'email' : 'scott@hotmail.com',
        'address' : '6 Skills City Lane, Manchester, M10 1BY',
        'acc_num' : '424400',
        'pin' : '1234',
        'balance' : 500
    },

    "joseph" : {
        'first_name' : 'Joseph',
        'last_name' : 'Rolins',
        'email' : 'jrolins@hotmail.com',
        'address' : '114 Pivet Drive, Manchester, M50 4WV',
        'acc_num' : '909090',
        'pin' : '8888',
        'balance' : 3850
    }
}

# def welcome function
# welcome message
# input do you have an account
# if yes run login function
#elif run register function
#else print try again, run welcome function again

def welcome():
    print("Welcome to Atlantic Bank")
    acc = input("Do you have an account? ")
    if acc.lower() == 'yes':
        login()
    elif acc.lower() == 'no':
        register()
    else:
        print('Please answer yes or no')
        welcome()

# def login function
# input acc num
# input pin
# if not dict key value pair in user_ids, run register function
# if a match, run menu function

def login():
    global first_name, last_name, email, address, acc_num, pin, balance, database
    acc_num = (input("Please enter your account number: "))
    pin = (input("Please enter your PIN number: "))
    for key, value in database.items():
        if acc_num == value['acc_num'] and pin == value['pin']:
            first_name = value['first_name']
            last_name = value['last_name']
            email = value['email']
            address = value['address']
            acc_num = value['acc_num']
            pin = value['pin']
            balance = value['balance']
            print(f'{first_name}, {last_name}, {email}, {address}, {acc_num}, {pin}, {balance}')
            print("Login Succesful")
            menu()
    print(f"Account number or PIN invalid, Please try again.")
    login()


#def register function
#register page
#collect email, fullname, password for database
#randomly generate 4 digit pin and 6 digit account number
#append name and pin as key, value pair to user_ids
# possibly randomly generate acc number to pair pin instead of using name
#create starting balance of 0
#run login function

def register():
    global database
    print("Please register your account by entering the details below")
    reg_first_name = input("Pleae enter your first name: ")
    reg_last_name = input('Please enter your last name: ')
    reg_email = input('Please enter your email address: ')
    reg_address = input('Please enter your address: ')
    reg_acc_num = (random.randint(100000, 999999))
    reg_pin = (random.randint(1000, 9999))
    while True:
        try:
            reg_balance = int(input('Please enter the amount of money you would like to depsoit to activate your account: '))
            break
        except ValueError:
            print("Pleae enter a valid number.")
            continue
    #append database with firstname as key in dictionary and all other information as value of that key
    database[reg_first_name] = {'first_name' : reg_first_name, 'last_name' : reg_last_name, 'email' : reg_email, 'address' : reg_address, 'acc_num' : str(reg_acc_num), 'pin' : str(reg_pin), 'balance' : reg_balance}
    print(f"You are now registered")
    print(f"Your account number is: {reg_acc_num} and your pin is {reg_pin}")
    print(f"Now redirecting you to the login page.. ")
    login()


#def withdraw function
#display balance
#input how much would you like to withdraw
#if amount <= balance, withdraw amount , display new balance
#else print error
#repeat ask if you would like to withdraw
#if no run menu function

def withdraw():
    global balance
    print(f"Your balance is: £{balance}")
    while True:
        try:
            amount = int(input("How much would you like to withdraw? "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if balance >= int(amount):
            print(f"Withdrawing... £{amount}")
            balance = balance - int(amount)
            print(f"Your remaining blance is £{balance}")
            menu()
        else:
            print("Sorry, you do not have sufficient funds.")
            menu()


#def deposit function
#display balance
#set a max deposit
#input how much would you like to deposit
#update balance
#print new balance
#run menu function

def deposit():
    global balance
    max_deposit = 5000
    amount = None
    print(f"Your balance is: £{balance}")
    while True:
        try:
            amount = int(input("How much would you like to deposit? "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if amount <= max_deposit:
            balance += amount
            print(f"Your new balance is £{balance}")
            menu()
        else:
            print(f"Sorry, the maximum deposit limit is £{max_deposit}. Please try again.")
            deposit()


# menu function
# on succesful login
# welcome customer
#bank menu (withdraw, deposit, show balance, send replacement card, exit)
#options run relevent function

def menu():
    global balance, first_name, last_name
    print(f'Welcome to Atlantic Bank {first_name.capitalize()} {last_name.capitalize()}.')
    answer = input(f"What service would you like to access? (withdraw, deposit, balance, send replacement card or exit) ")
    if answer.lower() == 'deposit':
        deposit()
    elif answer.lower() == 'withdraw':
        withdraw()
    elif answer.lower() == 'balance':
        print(f"Your balance is £{balance}")
        menu()
    elif answer.lower() == 'send replacement card':
        send_replacement_card()
    elif answer.lower() == 'exit':
        sys.exit()
    else:
        print("Sorry, that is not a valid choice. Try again..")
        menu()


#def send replacement card function
#print message

def send_replacement_card():
    print(f"You have ordered a new bank card..")
    print(f"Your card will be delivered to {address}")
    menu()


#welcome() whole program should run off this one function
welcome()

#return to menu after each service