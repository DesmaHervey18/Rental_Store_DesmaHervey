from Disk import *
# import disk
from Core import *


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
        response = input('\nAre you an [em]ployee or a [cu]stomer?\n')
        if response == 'cu':
            customer()
        elif response == 'em':
            employee()
        else:
            print('****Please Try Again, Announcement 1****')


def customer():
    print('\nGreat!')
    response = input('\nWould you like to rent a car or buy one?\n')
    if response == 'yes, I would like to rent a car.':
        load_inventory(inventory)
        response = input('Which car would you like to rent?')
        print(inventory)
        if response == 'Camaro 2018':
            print('1200')
            camaro_2018()
        elif response == 'Audi r8':
            print('14300')
            audi_r8()
        elif response == 'Bugatti Chiron':
            print('15500')
            bugattI_chiron()
        response = input('\nHow many days would you like to ')


def employee():
    print('\nHey, employee!\n')
    response = input('\nWould you like to view the inventory?\n')
    if response == 'yes':
        print(inventory)
        exit()
    elif response == 'no':
        print('\nThAnK YoU, Have a Blessed day!\n')
        exit()
    elif response == 'quit':
        print('\nHave a Blessed day!\n')
    exit()
    # else:
    #     print('\nPlease provide an valid answer cause your is invalid!\n')


def rental_payments():
    def main():
        inventory = open_inventory()
        print('\n~*~*~ Welcome to Desma\'s Rental Shop ~*~*~\n')
        which()
        customer()
        employee()
        rental_payments()

    # response = input('\nAre you an employee or a customer?\n')
    # if response == 'customer':
    #     print('\nGreat!')
    #     response = input('\nWould you like to rent a car or buy one?\n')
    #     if response == 'yes, I would like to rent a car.':
    #         load_inventory(inventory)
    #         response = input('\nWhich car would you like to rent?\n')
    #         which = input 'Audi r8'
    #         response = input('How many days would you like to rent the car?')

    # elif response == 'employee':
    #     print('\nHey, employee!\n')
    #     response = input('\nWould you like to view the inventory?\n')
    #     if response == 'yes':
    #         print(inventory)
    #         exit()
    #     elif response == 'no':
    #         print('\nThAnK YoU, Have a Blessed day!\n')
    #         exit()
    # elif response == 'quit':
    #     print('\nHave a Blessed day!\n')
    #     exit()
    # else:
    #     print('\nPlease provide an valid answer cause your is invalid!\n')

    # print_inventory(inventory)
    # save_inventory(inventory)


def main():
    if __name__ == '__main__':
        main()
