from datetime import datetime

import bankaccount_covid19
import bankaccount_covid19_company
import bankaccount_int


def create_customers():
    name = input('Hello, what is your name? ')
    print('Good morning ' + name + '!')

    date = datetime.now()
    date_1april = datetime(2020, 4, 1)
    is_later_than_1april = date > date_1april
    if is_later_than_1april:
        print('Today is ' + date.strftime('%Y-%m-%d') + ', so is later than 1 April')
    else:
        print('Today is ' + date.strftime('%Y-%m-%d') + ', so is earlier than 1 April')

    has_next_customer = True
    customers = []
    while has_next_customer is not False:
        print('For who do you want create the bank account?')
        try:
            choice = float(input('1 - Polish citizen, 2 - Polish company, 3 - Foreigner: '))
        except ValueError:
            print('You can choose only 1, 2 or 3!')
            choice = float(input('1 - Polish citizen, 2 - Polish company, 3 - Foreigner: '))
        is_good_choice = False
        is_correct = False
        while is_good_choice is not True:
            if choice == 1:
                while is_correct is not True:
                    first_name = input('Enter the customer first name: \n')
                    last_name = input('Enter the customer last name: \n')
                    try:
                        start_balance = float(input('Enter the customer start balance: \n'))
                    except ValueError:
                        start_balance = float(
                            input('You can use only the digits! Enter the customer start balance: \n'))
                    customer = bankaccount_covid19.BankAccount_COVID19(first_name, last_name, start_balance)
                    print('You have created: ')
                    print(customer)
                    correct = input(
                        'Do you want to correct the data? \'y\' to make corrects, \'o\' to make some operations, '
                        'any other to accept the customer \n')
                    if correct.lower() == 'o':
                        operations(customer)
                        is_correct = True
                        is_good_choice = True
                        customers.append(customer)
                    elif correct.lower() == 'y':
                        print('Enter the correct data')
                    else:
                        is_correct = True
                        is_good_choice = True
                        customers.append(customer)
            elif choice == 2:
                while is_correct is not True:
                    company_name = input('Enter the company name: \n')
                    try:
                        start_balance = float(input('Enter the customer start balance: \n'))
                    except ValueError:
                        start_balance = float(
                            input('You can use only the digits! Enter the customer start balance: \n'))
                    customer = bankaccount_covid19_company.BankAccount_COVID19_company(company_name, start_balance)
                    print('You have created: ')
                    print(customer)
                    correct = input(
                        'Do you want to correct the data? \'y\' to make corrects, \'o\' to make some operations, '
                        'any other to accept the customer \n')
                    if correct.lower() == 'o':
                        operations(customer)
                        is_correct = True
                        is_good_choice = True
                        customers.append(customer)
                    elif correct.lower() == 'y':
                        print('Enter the correct data')
                    else:
                        is_correct = True
                        is_good_choice = True
                        customers.append(customer)
            elif choice == 3:
                while is_correct is not True:
                    first_name = input('Enter the customer first name: \n')
                    last_name = input('Enter the customer last name: \n')
                    try:
                        start_balance = float(input('Enter the customer start balance: \n'))
                    except ValueError:
                        start_balance = float(
                            input('You can use only the digits! Enter the customer start balance: \n'))
                    customer = bankaccount_int.BankAccount_INT(first_name, last_name, start_balance)
                    print('You have created: \n {}'.format(customer))
                    correct = input(
                        'Do you want to correct the data? \'y\' to make corrects, \'o\' to make some operations, '
                        'any other to accept the customer \n')
                    if correct.lower() == 'o':
                        operations(customer)
                        is_correct = True
                        is_good_choice = True
                        customers.append(customer)
                    elif correct.lower() == 'y':
                        print('Enter the correct data')
                    else:
                        is_correct = True
                        is_good_choice = True
                        customers.append(customer)
            else:
                print('You can choose only between these possibilities!')
                choice = float(input('1 - Polish citizen, 2 - Polish company, 3 - Foreigner: \n'))
        next_customer = input(
            'Do you want to add the next customer? \'y\' for new customer, any other to stop adding \n')
        if next_customer.lower() != 'y':
            print('Customers which were created: ')
            for item in customers:
                print(item)
            return customers


def operations(customer):
    is_operation = True
    while is_operation is True:
        choice = float(input('1 - deposit, 2 - withdraw, 3 - close \n'))
        if choice == 1:
            amount = float(input('How much would you like to deposit? \n'))
            customer.deposit(amount)
            answer = input('Do you want make another operation? y or n \n')
            if answer.lower() == 'y':
                is_operation = True
            else:
                is_operation = False

        elif choice == 2:
            amount = float(input('How much would you like to withdraw? \n'))
            customer.withdraw(amount)
            answer = input('Do you want make another operation? y or n \n')
            if answer.lower() == 'y':
                is_operation = True
            else:
                is_operation = False
        elif choice == 3:
            customer.close()
            customer = None
            answer = input('Do you want make another operation? y or n \n')
            if answer.lower() == 'y':
                is_operation = True
            else:
                is_operation = False
