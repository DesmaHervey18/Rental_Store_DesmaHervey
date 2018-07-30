from disk import *
# import disk
from core import *
from daytime import daytime

def print_inventory(inventory):
    for item in inventory:
        print(inventory)


def load_inventory(inventory):
    for item in inventory:
        car = inventory[item]
        print(item)
        print('   rental:', car['rental'])
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


def which():
    while True:
        service = input('\nAre you an [em]ployee or a [cu]stomer?\n')
        if service_type == 'cu':
            customer()
        elif service_type == 'em':
            employee()
        else:
            print('****Invalid Answer, Please Try Again****')


def customer():
    print('\nGreat!')
    price = load_inventory(inventory)
    customer_service = input('\nWould you like to rent a car or buy one?\n')
    if customer_service == 'yes':
        print('I would like to rent a car.')
        load_inventory(inventory)
        car_type = input('Which car would you like to rent?')
        print(inventory)
        if car_type == 'Camaro 2018':
            price = 1200
            camaro_2018()
        elif == 'Audi r8':
            price = 14300
            audi_r8()
        elif == 'Bugatti Chiron':
            price = 15500
            bugatti_chiron()
        rent_length = input(
            '\nHow many days would you like to purchase this car?')
        
        return car_type
        return price
            

def write_to_transation_log(car_type, time, price):
    price = load_inventory(inventory)
    time = daytime.now()
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


def car_payment():
    if response == 'camaro_2018':
        print('Would you like to make a rental payment?')
        choice == 'yes'
        print('inventory rental cost')
        payment = input('Would you select your payment type?')
        if payment == 'A':
            cash()
        elif payment == 'B':
            debit()
        elif payment == 'C':
            credit()
        print('Dont forgive you\'ll have a rental fee if the car is late.')
        choice = input('Ok, I gotcha')
        print('Thank You and enjoy')
    else:
        choice == 'No'
        print('Thank You for shopping, we\'ll try again some other time.')
    if payment == 'audi r8':
        print('Would you like to make a rental payment?')
        payment == 'yes'
        print('inventory rental cost')
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
    if payment == 'bugatti chiron':
        print('inventory rental cost')
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


def main():
    inventory = open_inventory()
    print('\n~*~*~ Welcome to Desma\'s Rental Shop ~*~*~\n')
    which()
    customer()
    employee()
    rental_payments()
    camaro_2018()
    audi_r8()
    bugatti_chiron()
    write_to_transation_log(car_type, time, price)

if __name__ == '__main__':
    main()
