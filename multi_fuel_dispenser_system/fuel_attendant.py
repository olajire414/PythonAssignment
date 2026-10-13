
from multi_fuel_dispenser_system.fuel import Fuel


class Attendant:
    Fuel = Fuel()
    tank = []

    def __init__(self, full_name):
        self.full_name = full_name

    def get_full_name(self):
        return self.full_name

    def add_fuel(self, fuel):
        self.tank.append(fuel)














