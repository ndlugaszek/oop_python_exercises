# The BankAccount class simulates a bank account.
import random
import datetime
from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self):
        self.__account_number = random.randint(10000, 99999)
        self.__created_at = datetime.datetime.now()
        self.__is_open = True
        super(BankAccount, self).__init__()

    def __del__(self):
        print('The customer was deleted')

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def close(self):
        pass

    def get_account_number(self):
        return self.__account_number

    def get_created_at(self):
        year = str(self.__created_at.year)
        month = self.__created_at.month
        if month < 10:
            month = '0' + str(month)
        day = str(self.__created_at.day)
        date = year[2:4] + month + day
        return date

    def get_status(self):
        if self.__is_open:
            return 'open'
        else:
            return 'closed'

    def set_status(self):
        self.__is_open = False

    def __str__(self):
        return "{}; {}; {}" \
            .format(self.get_account_number(),
                    self.get_created_at(),
                    self.get_status())
