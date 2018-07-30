from disk import *
# import disk
from core import *
from datetime import datetime


def print_inventory(inventory):
    for item in inventory:
        print(inventory)


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
        print('I would like to rent a car.')
        c_inventory()
        car_type = input('Which car would you like to rent?\n')
        print(c_inventory)
        if car_payment == 'Charger 2018':
            price = 1200
            Charger_2018()
        elif car_payment == 'Audi r8':
            price = 14300
            audi_r8()
        elif car_payment == 'Bugatti 2018':
            price = 15500
            bugatti_2018()
        rent_length = input(
            '\nHow many days would you like to purchase this car?')


def car_payment():
    if customer_service == 'charger_2018':
        print('Would you like to make a rental payment?')
        customer_service == 'yes'
        print('inventory price')
        payment = input('Would you select your payment type?')
        if payment == 'A':
            cash()
        elif payment == 'B':
            debit()
        elif payment == 'C':
            credit()
        print('Dont forgive you\'ll have a rental fee if the car is late.')
        customer_service = input('Ok, I gotcha')
        print('Thank You and enjoy')
    else:
        customer_service == 'No'
        print('Thank You for shopping, we\'ll try again some other time.')
    if payment == 'audi r8':
        print('Would you like to make a rental payment?')
        payment == 'yes'
        print('inventory price')
        payment = input('Would you select your payment type?')
        if payment == 'A':
            cash()
        elif payment == 'B':
            debit()
        elif payment == 'C':
            credit()
        print('Dont forgive you\'ll have a rental fee if the car is late.')
        payment = input('Ok, I gotcha')
        print('Thank You and enjoy')
    else:
        payment == 'No'
        print('Thank You for shopping, we\'ll try again some other time.')
    if payment == 'bugatti 2018':
        print('inventory price')
        payment = input('Would you select your payment type?')
        if payment == 'A':
            cash()
        elif payment == 'B':
            debit()
        elif payment == 'C':
            credit()
        print('Dont forgive you\'ll have a rental fee if the car is late.')
        payment = input('Ok, I gotcha')
        print('Thank You and enjoy')
    else:
        payment == 'No'
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


def write_to_transation_log(car_type, time, price):
    price = car_inventory(inventory)
    time = datetime.now()
    text = '{},{},{}\n'.format(car_type, time, price)

    with open('history.txt', 'a') as file:
        file.write(text)


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
    # else:
    #     print('\nPlease provide an valid answer cause your is invalid!\n')


def main():
    inventory = car_inventory(inventory)
    print_inventory(inventory)
    which()
    customer()
    car_payment()
    car_inventory
    employee()
    write_to_transation_log(car_type, time, price())


if __name__ == '__main__':
    main()
