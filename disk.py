def open_inventory():
    with open('inventory.txt', 'r') as file:
        string = file.read()
    inventory = {}
    lines = string.split('\n')
    for line in lines:
        if line:
            d = parse_inventory_item(line)
            inventory[d[0]] = {
                'name': d[0],
                'in-stock': d[1],
                'price': d[2],
                'replacement_cost': d[3],
            }

    return inventory


def print_inventory(inventory):
    for item in inventory:
        print(item)


def car_inventory():
    with open('inventory.txt') as f:
        inventory = {}
        for line in f:
            name, in_stock, price_str, replacement_cost_str = line.split(',')
            item = {
                'name': name,
                'in_stock': int(in_stock_str),
                'price': int(price_str),
                'replacement_cost': int(replacement_cost_str),
            }
            inventory[name] = item
        return inventory


# def choose_car(inventory):
#     for item in inventory:
#         car = inventory[item]
#         print(item)
#         print('   name:', car['name'])
#         print('   in-stock:', car['in-stock'])
#         print('   price:', car['price'])
#         print('   replacement:', car['replacement'])


def choice_of_car(inventory):
    for items in inventory:
        car = inventory[item]
        print(item)
        print('     name:', car_type['name'])
        print('     in_stock:', car_type['in_stock'])
        print('     price:', car_type['price'])
        print('     replacement_cost:', car_type['replacement_cost'])


def parse_inventory_item(string):
    name, in_stock, price, replacement_cost = string.split
    return [str(name), int(in_stock), int(price)]


def save_inventory(inventory):
    with open('inventory.txt', 'w') as f:
        for item in inventory.values():
            f.write('{},{},{}\n'.format(
                item['name'],
                item['in_stock'],
                item['price'],
                item['replacement_cost'],
            ))
