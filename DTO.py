# Data Transfer Objects:
class Hats:
    def __init__(self, id, topping, supplier, quantity):
        self.id = id #primary key
        self.topping = topping
        self.supplier = supplier #reference to supplier id
        self.quantity = quantity


class Suppliers:
    def __init__(self, id, name):
        self.id = id #primary key
        self.name = name


class Orders:
    def __init__(self, id, location, hat):
        self.id = id #primary key
        self.location = location
        self.hat = hat #referecne key to hats(id)