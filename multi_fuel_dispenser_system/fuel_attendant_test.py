import unittest

from multi_fuel_dispenser_system.fuel import Fuel
from multi_fuel_dispenser_system.fuel_attendant import Attendant

class AttendantTestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.fuel = None

    def test_that_attendant_name_can_be_retrieved(self):
        self.attendant = Attendant("john")
        self.assertEqual("john", self.attendant.get_full_name())  # add assertion here

    def test_that_attendant_can_add_new_fuel(self):
        self.my_fuel = Fuel()
        self.attendant.add_fuel(self.my_fuel)



if __name__ == '__main__':
    unittest.main()
