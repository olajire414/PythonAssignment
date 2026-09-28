import unittest
from multi_fuel_dispenser_system import fuel_dispenser_app

class MyFuelDispenserTest(unittest.TestCase):

    def test_ihave_display_board_can_display_available_fuel(self):
        display_fuels = """ \nAvailable Petroleum\n 1. Petrol  => 650/Liter  \n 2. Diesel  => 720/Liter \n 3. Kerosene  => 720/Liter \n 4. Gas 480/Liter """
        self.assertEqual(display_fuels, fuel_dispenser_app.display_board())

    def test_that_customers_can_select_options_from_menu(self)->None:
        option = 2
        match option:
            case 1: "1. Petrol  => 650/Liter"
            case 2: "2. Diesel  => 720/Liter"
            case 3: "3. Kerosene  => 720/Liter"
            case 4: "4. Gas 480  => 720/Liter"

        self.assertEqual(option, fuel_dispenser_app.select_option(2))

    def test_that_customer_enters_amount_to_get_how_many_liter_of_fuel_to_buy(self)->None:
        amount = 5000
        price_per_liter = 720
        number_liter = amount/price_per_liter
        self.assertEqual(number_liter, fuel_dispenser_app.get_fuel_by_amount(amount,price_per_liter))

    def test_that_customer_enters_number_of_liter_to_get_fuel(self) -> None:
        number_of_liter = 5
        price_per_liter = 650
        amount = number_of_liter * price_per_liter
        self.assertEqual(amount, fuel_dispenser_app.get_fuel_by_number_of_liter(number_of_liter,price_per_liter))

    def test_that_calculate_total_cost_based_on_liter_inputted(self)->None:
        number_liter = 5
        cost_per_liter = 650
        total_cost = number_liter * cost_per_liter
        self.assertEqual(total_cost,fuel_dispenser_app.calc_total_cost_with_liter(number_liter,cost_per_liter))

    def test_that_calculate_total_cost_based_on_amount_inputted(self)->None:
        amount = 2000
        cost_per_liter = 720
        total_cost = amount / cost_per_liter
        self.assertEqual(total_cost,fuel_dispenser_app.calc_total_cost_with_amount(amount,cost_per_liter))

    def test_that_transaction_can_be_recorded(self, ):
        all_transactions = []
        product = "petrol"
        amount = 5000
        liter = "5L"


        transaction = {
            "product": product,
            "amount": amount,
            "liter": liter
        }
        all_transactions.append(transaction)
        self.assertEqual(all_transactions,fuel_dispenser_app.get_all_transaction_history(product,amount,liter))


if __name__ == '__main__':
    unittest.main()
