
class Fuel:



    def __init__(self) ->None:
        self.fuel_name = "petrol"
        self.fuel_price = 0
        self.fuel_quantity = 0


    def is_fuel_available(self):
        return self.fuel_quantity == 0


    def get_fuel_price(self):
        return self.fuel_price

    def get_fuel_name(self):
        return self.fuel_name

    def get_quantity(self):
        return self.fuel_quantity

    def set_fuel_price(self,price):
        self.fuel_price = price



    def set_fuel_name(self, name):
        self.fuel_name = name





