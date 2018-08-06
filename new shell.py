from core import *
from disk import *
from datetime import datetime


def welcome():
    print('*~*Welcome to Desma\'s Rental Company~*~')
    print('*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*')


def which():
    while True:
        service = input(
            '\nAre you a [cu]customer or an [em]employee? or quit!!\n')
        if service == 'cu':
            customer()
        if service == 'em':
            employee()
        elif service == 'quit':
            exit()
        else:
            print('**Invalid Answer, Please Try Again**')
    print('*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*')


def parse_inventory_item(string):
    name, in_stock, price, replacement_cost = string.split
    return [str(name), int(in_stock), int(price), int(replacement_cost)]


def customer():
    print('\nGreat!')
    inventory = c_inventory()
    price = c_inventory()
    customer_service = input(
        '\nWould you like to rent a car or buy one on today?\n')
    if customer_service == 'rent':
        print('Charger 2018')
        print('Audi r8')
        print('Bugatti 2018')
        customer_response = input('Which car would you like to rent?\n')
        inventory = c_inventory()
        if customer_response == 'Charger 2018':
            charger_2018()
        elif customer_response == 'Audi r8':
            audi_r8()
        elif customer_response == 'Bugatti 2018':
            bugatti_2018()
        rent_length = input(
            '\nHow many days would you like to purchase this car?\n')
        print(
            'You\'ll have a rental fee in {} days, if late that\'ll be a $200 fee each day it\'s late. '.
            format(rent_length))

    write_to_transation_log(customer_response)
    return customer_response


def print_inventory(inventory):
    for item in inventory:
        print(item)


def c_inventory():
    inventory = [{
        'name': 'Charger 2018',
        'in-stock': 5,
        'price': 1200,
        'replacement cost': 650
    }, {
        'name': 'Audi r8',
        'in-stock': 3,
        'price': 14300,
        'replacement cost': 700
    }, {
        'name': 'Bugatti 2018',
        'in-stock': 4,
        'price': 15500,
        'replacement cost': 750
    }]
    return inventory


def charger_2018():
    if customer_response == 'CHARGER 2018':
        customer_service = input(
            'Would you like to make a rental payment?\n').upper().strip()
        customer_service == 'YES'
        print(
            'Don\'t forget that you\'ll have a rental fee if the car is late or damage, once returned'
        )
        customer_service = input('Ok, I gotcha')
        print('Thank You and enjoy.')
    else:
        customer_service == 'No'
        print('Thank You for coming, we can try again some other time.')


def audi_r8():
    if customer_response == 'AUDI r8':
        customer_service = input(
            'Would you like to make a rental payment?\n').upper().strip()
        customer_service == 'YES'
        print(
            'Don\'t forget that you\'ll have a rental fee if the car is late or damage, once returned'
        )
        customer_service = input('Ok, I gotcha')
        print('Thank You and enjoy.')
    else:
        customer_service == 'No'
        print('Thank You for coming, we can try again some other time.')


def bugatti_2018():
    if customer_response == 'BUGATTI 2018':
        customer_service = input(
            'Would you like to make a rental payment?\n').upper().strip()
        customer_service == 'YES'
        print(
            'Don\'t forget that you\'ll have a rental fee if the car is late or damage, once returned'
        )
        customer_service = input('Ok, I gotcha')
        print('Thank You and enjoy.')
    else:
        customer_service == 'No'
        print('Thank You for coming, we can try again some other time.')


def employee():
    print('\nHi!\n')
    response = input('\nWould you like to view the inventory?\n')
    if response == 'yes':
        inventory = c_inventory()
        print(inventory)
        exit()
    elif response == 'no':
        print('\nThAnK YoU,\n')
        exit()
    elif response == 'quit':
        print('\nHave a good day!\n')
    exit()


def car_inventory(inventory):
    for item in inventory:
        car_inventory[item]
        print(item)
        print('   name:', car['name'])
        print('   in-stock:', car['in-stock'])
        print('   price:', car['price'])
        print('   replacement:', car['replacement'])
    while True:
        item = input('\nWhich car would you like to purchase?\n')
        if item in inventory:
            print('That\'s an amazing choice!')
            exit()
        elif item == 'quit':
            break
        else:
            print(
                '\nSorry we DO NOT have this stock please choose another car, if you dont mind.\n'
            )


def write_to_transation_log(customer_response):
    time = datetime.now()
    text = '{},{}\n'.format(customer_response, time)

    with open('history.txt', 'a') as file:
        file.write(text)


def save_inventory(inventory):
    with open('inventory.txt', 'w') as f:
        for item in inventory.values():
            f.write('{},{},{}\n'.format(
                item['name'],
                item['in_stock'],
                item['price'],
                item['replacement_cost'],
            ))
            return history


def main():
    welcome()
    which()
    parse_inventory_item(string)
    customer()
    print_inventory(inventory)
    c_inventory()
    charger_2018()
    audi_r8()
    bugatti_2018()
    employee()
    car_inventory(inventory)
    save_inventory(inventory)
    if service == 'quit':
        exit()


if __name__ == '__main__':
    main()
