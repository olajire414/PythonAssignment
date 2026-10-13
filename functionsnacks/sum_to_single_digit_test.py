import unittest
from functionsnacks import sum_to_single_code


class SumToSingleDigitTest(unittest.TestCase):
    def test_that_digits_floor_division_is_987(self):
        digits = 9875
        digit = 987
        self.assertEqual(digit, sum_to_single_code.sum_digit_to_single_number())







        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
