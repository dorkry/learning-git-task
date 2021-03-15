#magazyn

import logging
logging.basicConfig(level=logging.INFO)

items = []
item1 = {
    "name": "coffee", 
    "quantity": 30,
    "unit": "kg",
    "unit_price": 69.99
}
items.append(item1)

item2 = {
    "name": "tea", 
    "quantity": 45,
    "unit": "kg",
    "unit_price": 21.00
}
items.append(item2)

item3 = {
    "name": "sugar", 
    "quantity": 14,
    "unit": "kg",
    "unit_price": 3.99
}
items.append(item3)


def close(a):
    return 0

def get_items(shop_list):
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("------\t--------\t----\t---------- ")
    for item in shop_list:
        print(f"{item['name']}\t{item['quantity']}\t\t{item['unit']}\t{item['unit_price']}")
    return shop_list

def add(shop_list):
    print("Adding to warehouse...")
    new_name = input("Item name: ")
    new_quantity = input("Item quantity: ")
    new_unit = input("Item unit: ")
    new_price = input("Item price: ")
    new_item = {
        "name": new_name,
        "quantity": new_quantity,
        "unit": new_unit,
        "unit_price": new_price
    }
    shop_list.append(new_item)
    return shop_list
    
menu = {
 "exit": close,
 "show": get_items,
 "add": add
}

if __name__ == "__main__":
    while True:
        choice = input("What do you want to do?")
        try:
            menu_func = menu[choice]
        except KeyError:
            print("Unknown action")
        else:    
            items = menu_func(items)
            if items == 0:
                print("Thank you! Bye!")
                break
