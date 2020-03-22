# The BankAccount class simulates a bank account.
import random
import datetime


class BankAccount:
    # The __init__ method creates an object with random account number, date of creation and status set to 'o' - opened.
    # The parameters which the user need to input is the name of the customer and starting balance do the account
    def __init__(self, first_name, last_name, bal):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = random.randint(100000, 999999)
        self.__balance = bal
        self.__created_at = datetime.datetime.now()
        self.__status = 'o'

    # The deposit method makes a deposit into the account.
    def deposit(self, amount):
        good_value = False
        while good_value is not True:
            try:
                self.__balance += amount
                good_value = True
            except ValueError:
                print('Wrong input! Please, use only the digits!')
                good_value = False

    # The withdraw method withdraws an amount from the account.
    def withdraw(self, amount):
        good_value = False
        while good_value is not True:
            try:
                if self.__balance >= amount:
                    self.__balance -= amount
                else:
                    print('Error: Insufficient funds')
                good_value = True
            except ValueError:
                print('Wrong input! Please, use only the digits!')
                good_value = False

    # The getters methods returns the account information
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_created_at(self):
        year = str(self.__created_at.year)
        month = self.__created_at.month
        if month < 10:
            month = '0' + str(month)
        day = str(self.__created_at.day)
        date = year[2:4] + month + day
        return date

    def get_status(self):
        return self.__status
