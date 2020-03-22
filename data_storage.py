import csv
import pickle
import bankaccount


# The code of the first exercise
def print_balance(savings):
    print('Your account balance is $',
          format(savings.get_balance(), ',.2f'),
          sep='')


# The method which create the customer
def create_customer():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    good_value = False
    while good_value is not True:
        try:
            start_bal = float(input('Enter starting balance: '))
            good_value = True
        except ValueError:
            print('Wrong input! Please, use only the digits!')
            good_value = False

    # Create a BankAccount object.
    customer = bankaccount.BankAccount(first_name, last_name, start_bal)

    # Deposit the user's paycheck.
    money = account_operation('deposit')
    print('I will deposit that into your account.')
    customer.deposit(money)

    # Display the balance.
    print_balance(customer)

    # Get the amount to withdraw.
    money = account_operation('withdraw')
    print('I will withdraw that from your account.')
    customer.withdraw(money)

    # Display the balance.
    print_balance(customer)

    return customer


# The method which create the data of the customer
def create_data(customer):
    return {'Imie': customer.get_first_name(),
            'Nazwisko': customer.get_last_name(),
            'Numer_rachunku': customer.get_account_number(),
            'Saldo': customer.get_balance(),
            'Data_otwarcia': customer.get_created_at(),
            'Status': customer.get_status()
            }


# The method which makes the operation deposit or withdraw
def account_operation(operation):
    money = 0
    good_value = False
    while good_value is not True:
        try:
            if operation == 'deposit':
                money = float(input('How much would you like to deposit? '))
            elif operation == 'withdraw':
                money = float(input('How much would you like to withdraw? '))
            good_value = True
        except ValueError:
            print('Wrong input! Please, use only the digits!')
            good_value = False
    return money


# The method which writes and reads data to the CSV file
def read_write_csv_file():
    again = 'y'
    # Open the csv file with write
    csv_file = open('bank_account.csv', 'w')

    with csv_file:
        # Crete and set the fields name in the csv file
        field_names = ['Imie', 'Nazwisko', 'Numer_rachunku', 'Saldo', 'Data_otwarcia', 'Status']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        while again.lower() == 'y':
            customer = create_customer()
            # Write the BankAccount object to the csv file
            writer.writerow(create_data(customer))
            again = input('Do you want to add next customer(y/n)? ')
        csv_file.close()
        # Open the file in the read mode
        csv_file = open('bank_account.csv', 'r')
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)
        csv_file.close()


# The method which writes and reads data to the PICKLE file
def read_write_pickle_file():
    again_pickle = 'y'
    # Open the PICKLE file in write mode
    bin_file = open('bank_accounts', 'wb')
    bank_account_data = {}

    while again_pickle.lower() == 'y':
        # Create the customer and write it to the file
        bank_account_data.update(create_data(create_customer()))
        pickle.dump(bank_account_data, bin_file)
        again_pickle = input('Do you want to add next customer(y/n)? ')
    bin_file.close()
    # Open the PICKLE file in read mode
    bin_file = open('bank_accounts', 'rb')
    end_of_file = False
    # Print all the objects from the file
    while not end_of_file:
        try:
            print(pickle.load(bin_file))
        except EOFError:
            end_of_file = True
    bin_file.close()
