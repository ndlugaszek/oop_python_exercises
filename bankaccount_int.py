from bankaccount import BankAccount
from customer_type import CustomerType


class BankAccount_INT(BankAccount):

    def __init__(self, first_name, last_name, start_balance):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = start_balance
        self.__customer_type = CustomerType.FOREIGNER.value
        BankAccount.__init__(self)

    def deposit(self, amount):
        good_value = False
        while good_value is not True:
            try:
                self.__balance += amount
                good_value = True
                print('Your balance is {}'.format(self.get_balance()))
            except ValueError:
                print('Wrong input! Please, use only the digits!')
                good_value = False

    def withdraw(self, amount):
        good_value = False
        while good_value is not True:
            try:
                if self.__balance >= amount:
                    self.__balance -= amount
                    print('Your balance is {}'.format(self.get_balance()))
                else:
                    print('Error: Insufficient funds')
                good_value = True
            except ValueError:
                print('Wrong input! Please, use only the digits!')
                good_value = False

    def close(self):
        if self.__balance > 0:
            self.withdraw(self.get_balance())
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

    def __str__(self):
        return "Customer: {}; {}; {}; {}; " \
                   .format(self.get_first_name(),
                           self.get_last_name(),
                           self.get_balance(),
                           self.get_customer_type()) \
               + super().__str__()
