from disk import *
from core import *

# from datetime import datetime


def which():
    while True:
        service = input('\nAre you an [em]employee or a [cu]customer?\n')
        if service == 'cu':
            customer()
        elif service == 'em':
            employee()
        else:
            print('****Invalid Answer, Please Try Again****')


def customer():
    print('\nGreat!')
    price = c_inventory()
    customer_service = input('\nWould you like to rent a car or buy one?\n')
    if customer_service == 'rent':
        print('Charger 2018')
        print('Audi r8')
        print('Bugatti 2018')
        car_type = input('Which car would you like to rent?\n')
        inventory = car_inventory()
        if customer_service == 'Charger 2018':
            charger_2018()
        elif customer_service == 'Audi r8':
            audi_r8()
        elif customer_service == 'Bugatti 2018':
            bugatti_2018()
        rent_length = input(
            '\nHow many days would you like to purchase this car?')


def charger_2018():
    if customer_service == 'charger_2018':
        customer_service = input('Would you like to make a rental payment?')
        customer_service == 'yes'
        print('Dont forget you\'ll have a rental fee if the car is late.')
        customer_service = input('Ok, I gotcha')
        print('Thank You and enjoy')
    else:
        customer_service == 'No'
        print('Thank You for shopping, we\'ll try again some other time.')


def audi_r8():
    if customer_service == 'audi r8':
        customer_service = input('Would you like to make a rental payment?')
        customer_service == 'yes'
        print('Dont forget you\'ll have a rental fee if the car is late.')
        customer_service = input('Ok, I gotcha')
        print('Thank You and enjoy')
    else:
        customer_service == 'No'
        print('Thank You for shopping, we\'ll try again some other time.')


def bugatti_2018():
    if customer_service == 'bugatti 2018':
        customer_service = input('Would you like to make a rental payment?')
        customer_service == 'yes'
        print('Dont forget you\'ll have a rental fee if the car is late.')
        customer_service = input('Ok, I gotcha')
        print('Thank You and enjoy')
    else:
        customer_service == 'No'
        print('Thank You for shopping, we\'ll try again some other time.')


def car_inventory(inventory):
    for item in inventory:
        car = inventory[item]
        print(item)
        print('   name:', car['name'])
        print('   in-stock:', car['in-stock'])
        print('   price:', car['price'])
        print('   replacement:', car['replacement'])
    while True:
        item = input('\nWhich car would you like?\n')
        if item in inventory:
            print('That\'s an amazing choice!')
            exit()
        elif item == 'quit':
            break
        else:
            print(
                '\nSorry we do not have this in stock please choose another car!\n'
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
    which()
    customer()


if __name__ == '__main__':
    main()
