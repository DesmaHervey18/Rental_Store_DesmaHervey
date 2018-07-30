def open_inventory():
    with open('Inventory.txt', 'r') as file:
        string = file.read()
    inventory = {}
    lines = string.split('\n')
    for line in lines:
        if line:
            d = parse_inventory_item(line)
            inventory[d[0]] = {
                'rent': d[0],
                'in-stock': d[1],
                'price': d[2],
                'replacement cost': d[3],
            }

    return inventory


def print_inventory(inventory):
    for item in inventory:
        print(item)


def desma_inventory():
    with open('inventory.txt') as f:
        inv = {}
        for line in f:
            name, price_str, quant_str = line.split(',')
            item = {
                'name': name,
                'price': int(price_str),
                'quantity': int(quant_str),
            }
            inv[name] = item
        return inv


def choose_car(inventory):
    for item in inventory:
        car = inventory[item]
        print(item)
        print('   rent:', car['rent'])
        print('   in-stock:', car['in-stock'])
        print('   price:', car['price'])


def parse_inventory_item(string):
    rental, in_stock, price = string.split(',')
    return [rent, int(in_stock), int(price)]


def save_inventory(inventory):
    with open('inventory.txt', 'w') as f:
        for item in inventory.values():
            f.write('{},{},{}\n'.format(
                item['name'],
                item['price'],
                item['quantity'],
            ))
