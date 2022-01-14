from DTO import Hats, Suppliers
from Repository import repo

import os

def start(config_path, orders_path):
    repo.__init__()
    repo.create_tables()
    with open(config_path) as config:
        firstline = config.readline()
        param = firstline.split()[0]
        param = param.split(",")
        num_of_hats = (int)(param[0])
        num_of_suppliers = (int)(param[1])
        lines = config.readlines()
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

    # while(range(num_of_suppliers - 1) != num_of_suppliers):
    #     (id, name) = os.path.splitext(os.listdir(config_path))
    #     supplier = Suppliers.__init__(id, name)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        start("config.txt", "orders.txt")

