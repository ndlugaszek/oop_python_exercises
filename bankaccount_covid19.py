from bankaccount import BankAccount
from customer_type import CustomerType


class BankAccount_COVID19(BankAccount):

    def __init__(self, first_name, last_name, start_balance):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = start_balance
        self.__customer_type = CustomerType.INDIVIDUAL.value
        self.__day_limit = 1000
        BankAccount.__init__(self)

    def deposit(self, amount):
        good_value = False
        while good_value is not True:
            try:
                self.__balance += amount
                print('Your balance is {}'.format(self.get_balance()))
                good_value = True
            except ValueError:
                print('Wrong input! Please, use only the digits!')
                good_value = False

    def withdraw(self, amount):
        print('ATTENTION! You can only make payments, ATM withdrawal is on hold!')
        good_value = False
        while good_value is not True:
            try:
                if self.__day_limit >= 1000 and amount <= self.get_day_limit():
                    if self.__balance >= amount:
                        self.__balance -= amount
                        self.__day_limit -= amount
                        print('Your balance is {} and day limit is {}'.format(self.get_balance(), self.get_day_limit()))
                    else:
                        print('Error: Insufficient funds')
                else:
                    print('Insufficient daily limit! Available limit: {}'.format(self.get_day_limit()))
                good_value = True
            except ValueError:
                print('Wrong input! Please, use only the digits!')
                good_value = False

    def close(self):
        if self.__balance > 0:
            self.set_day_limit()
            self.withdraw(self.__balance)
        self.set_status()
        print('Your account was closed')
        self.__del__()

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_balance(self):
        return self.__balance

    def get_customer_type(self):
        return self.__customer_type

    def get_day_limit(self):
        return self.__day_limit

    def set_day_limit(self):
        self.__day_limit = self.get_balance()

    def __str__(self):
        return "Customer: {}; {}; {}; {}; {}; " \
                   .format(self.get_first_name(),
                           self.get_last_name(),
                           self.get_balance(),
                           self.get_customer_type(),
                           self.get_day_limit()) \
               + super().__str__()
