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


def create_file_string(c_inventory):
    ''' {str: int} -> str
    turns the user_dictionary into a string
    '''
    file_string = 'name, in_stock, price, replacement'
    for name, in_stock, price, replacement in user_dictionary.items():
        file_string += '\n{}, {}, {}, {}'.format(name, in_stock, price,
                                                 replacement)

    return file_string


def save_inventory(inventory):
    with open('inventory.txt', 'w') as f:
        for item in inventory.values():
            f.write('{},{},{}\n'.format(
                item['name'],
                item['in_stock'],
                item['price'],
                item['replacement_cost'],
            ))


def get_vehicleprice():
    if customer_service == 'CHARGER 2018':
        price = 1200
    if customer_service == 'AUDI 2018':
        price = 14300
    if customer_service == 'BUGATTI 2018':
        price = 15500
