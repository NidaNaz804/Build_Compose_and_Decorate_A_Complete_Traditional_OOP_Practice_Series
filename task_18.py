# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, 
# and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

item = Product(100)
print(item.price)
item.price = 150
print(item.price)
del item.price
