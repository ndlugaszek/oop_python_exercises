import csv
import create_customers


def read_customers():
    customers = []
    for customer in create_customers.create_customers():
        customers.append(customer)
    return customers


def create_data(customer):
    if hasattr(customer, 'get_first_name') is not True:
        return {'Nazwa': customer.get_company_name(),
                'Saldo': customer.get_balance(),
                'Typ klienta': customer.get_customer_type(),
                'Nr rachunku': customer.get_account_number(),
                'Data otwarcia': customer.get_created_at(),
                'Status': customer.get_status()}
    elif hasattr(customer, 'get_day_limit') is not True:
        return {'Imie': customer.get_first_name(),
                'Nazwisko': customer.get_last_name(),
                'Saldo': customer.get_balance(),
                'Typ klienta': customer.get_customer_type(),
                'Nr rachunku': customer.get_account_number(),
                'Data otwarcia': customer.get_created_at(),
                'Status': customer.get_status()}
    else:
        return {'Imie': customer.get_first_name(),
                'Nazwisko': customer.get_last_name(),
                'Saldo': customer.get_balance(),
                'Typ klienta': customer.get_customer_type(),
                'Limit dzienny': customer.get_day_limit(),
                'Nr rachunku': customer.get_account_number(),
                'Data otwarcia': customer.get_created_at(),
                'Status': customer.get_status()}


def read_write_csv_file():
    csv_file = open('bank_account.csv', 'w')

    with csv_file:
        field_names = ['Imie', 'Nazwisko', 'Nazwa', 'Saldo',
                       'Typ klienta', 'Limit dzienny', 'Nr rachunku',
                       'Data otwarcia', 'Status']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for customer in read_customers():
            writer.writerow(create_data(customer))
        csv_file.close()
        csv_file = open('bank_account.csv', 'r')
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)
        csv_file.close()
