from DTO import Hats, Suppliers, Orders
from Repository import repo

import os

def start(config_path, orders_path):
    repo.create_tables()
    with open('Summary.txt', 'w') as summary:
        with open(config_path) as config:
            firstline = config.readline()
            param = firstline.split()[0]
            param = param.split(",")
            num_of_hats = (int)(param[0])
            num_of_suppliers = (int)(param[1])
            lines = config.readlines()
            count = 1
            for line in lines:
                if num_of_hats != 0:
                    hat_details = line.split()[0]
                    hat_details = line.split(",")
                    id = (int)(hat_details[0])
                    topping = hat_details[1]
                    supplier = (int)(hat_details[2])
                    quantity = (int)(hat_details[3])
                    num_of_hats = num_of_hats - 1
                    hat = Hats(id, topping, supplier, quantity)
                    repo.hats.insert(hat)
                elif num_of_suppliers != 0:
                    supplier_details = line.split()[0]
                    supplier_details = line.split(",")
                    id = (int)(supplier_details[0])
                    name = supplier_details[1]
                    if count != len(lines):
                        name = name[0:len(name) - 1]
                    num_of_suppliers = num_of_suppliers - 1
                    supplier = Suppliers(id, name)
                    repo.suppliers.insert(supplier)
        with open(orders_path) as orders:
            lines = orders.readlines()
            orderid = 1
            count = 1
            for line in lines:
                order_details = line.split()[0]
                order_details = line.split(",")
                location = order_details[0]
                topping = order_details[1]
                if count != len(lines):
                    topping = topping[0:len(topping)-1]
                hats = repo.hats.findall(topping)
                hat_id = findminsupplier(hats)
                hat = repo.hats.find(hat_id)
                quantity = hat.quantity - 1
                if quantity == 0:
                    repo.hats.remove(hat_id)
                supplier = repo.suppliers.find(hat.supplier)
                summary.write(f'{topping},{supplier.name},{location}\n')
                repo.hats.update(quantity, hat_id)
                count = count + 1
                repo.orders.insert(Orders(orderid, location, topping))
                orderid = orderid + 1





def findminsupplier(list_of_tuples):
    supplier_id = list_of_tuples[0][2]
    hat_id = list_of_tuples[0][0]
    for hat in list_of_tuples:
        if hat[2] < supplier_id:
            hat_id = hat[0]
    return hat_id

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        start("config.txt", "orders.txt")

