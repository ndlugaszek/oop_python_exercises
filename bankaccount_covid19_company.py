from bankaccount import BankAccount
from customer_type import CustomerType


class BankAccount_COVID19_company(BankAccount):

    def __init__(self, company_name, start_balance):
        self.__company_name = company_name
        self.__balance = start_balance + 5000
        self.__customer_type = CustomerType.COMPANY.value
        self.__government_loan = True
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
        if self.get_government_loan():
            print('Due to government loan, you cannot close your account!')

    def get_company_name(self):
        return self.__company_name

    def get_balance(self):
        return self.__balance

    def get_customer_type(self):
        return self.__customer_type

    def get_day_limit(self):
        return self.__day_limit

    def get_government_loan(self):
        return self.__government_loan

    def __str__(self):
        return "Customer: {}; {}; {}; {}; {}; " \
                   .format(self.get_company_name(),
                           self.get_balance(),
                           self.get_customer_type(),
                           self.get_day_limit(),
                           self.get_government_loan()) \
               + super().__str__()
