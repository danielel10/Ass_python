# Data Access Objects:
# All of these are meant to be singletons
from DTO import Hats, Suppliers, Orders


class _Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
               INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def findall(self, _topping):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, topping, supplier, quantity FROM hats WHERE topping = ?
        """, [_topping])

        return c.fetchall()

    def find(self, _id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, topping, supplier, quantity FROM hats WHERE id = ?
        """, [_id])

        return Hats(*c.fetchone())

    def update(self, _quantity, _id):
        self._conn.execute("""
                       UPDATE hats SET quantity=(?) WHERE id=(?)
                   """, [_quantity, _id])

    def remove(self, _id):
        self._conn.execute("""
                DELETE FROM hats   WHERE id=(?) 
        """, [_id])


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO suppliers (id, name) VALUES (?, ?)
        """, [supplier.id, supplier.name])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,name FROM suppliers WHERE id = ?
            """, [id])

        return Suppliers(*c.fetchone())


class _Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
            INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
        """, [order.id, order.location, order.hat])

    def findall(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, location, hat FROM orders
        """)

        return c.fetchall()
