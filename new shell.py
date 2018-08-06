from disk import *
# import disk
from core import *
from datetime import datetime


def welcome():
    print('*~*Welcome to Desma\'s Rental Company~*~')
    print('*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*')


def which():
    while True:
        service = input('\nAre you a [cu]customer or an [em]employee?\n')
        if service == 'cu':
            customer()
        elif service == 'em':
            employee()
        else:
            print('**Invalid Answer, Please Try Again**')
    print('*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*')


def customer():
    print('\nGreat!')
    price = c_inventory()
    customer_service = input(
        '\nWould you like to rent a car or buy one on today?\n')
    if customer_service == 'rent':
        print('Charger 2018')
        print('Audi r8')
        print('Bugatti 2018')
        car_type = input('Which car would you like to rent?\n')
        inventory = c_inventory()
        if customer_service == 'Charger 2018':
            charger_2018()
        elif customer_service == 'Audi r8':
            audi_r8()
        elif customer_service == 'Bugatti 2018':
            bugatti_2018()
        rent_length = input(
            '\nHow many days would you like to purchase this car?\n')


def charger_2018():
    if customer_service == 'Charger_2018':
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
    if customer_service == 'Audi_r8':
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
    if customer_service == 'Bugatti_2018':
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


def save_inventory(inventory):
    with open('inventory.txt', 'w') as f:
        for item in inventory.values():
            f.write('{},{},{}\n'.format(
                item['name'],
                item['in_stock'],
                item['price'],
                item['replacement_cost'],
            ))


def main():
    welcome()
    which()
    customer()
    charger_2018()
    audi_r8()
    bugatti_2018()
    employee()
    car_inventory(inventory)
    save_inventory(inventory)


if __name__ == '__main__':
    main()
