import unittest
from multi_fuel_dispenser_system.fuel import Fuel

class FuelTest(unittest.TestCase):

    def test_that_fuel_quantity_can_measured(self):
        self.my_fuel = Fuel()
        self.my_fuel.set_fuel_quantity("600L")
        self.assertEqual("600L",self.my_fuel.get_quantity())


    def test_that_can_fuel_name(self):
        self.my_fuel = Fuel()
        #self.my_fuel.set_fuel_name('petrol')
        self.assertAlmostEqual('petrol',self.my_fuel.get_fuel_name())

    def test_that_fuel_price_can_be_set(self):
        self.my_fuel = Fuel()
        self.my_fuel.set_fuel_price(550)
        self.assertAlmostEqual(550, self.my_fuel.get_fuel_price())


if __name__ == '__main__':
    unittest.main()
