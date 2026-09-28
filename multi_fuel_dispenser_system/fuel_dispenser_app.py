
all_transactions = []
from datetime import date

def display_board():
    display_fuels =  """ \nAvailable Petroleum\n 1. Petrol  => 650/Liter  \n 2. Diesel  => 720/Liter \n 3. Kerosene  => 720/Liter \n 4. Gas 480/Liter """

    return display_fuels

def select_option(option):

    match option:
        case 1:"1. Petrol  => 650/Liter"
        case 2: "2. Diesel  => 720/Liter"
        case 3:"3. Kerosene  => 720/Liter"
        case 4:"4. Gas 480  => 720/Liter"
    return option


def get_fuel_by_amount(amount,price_per_liter):
    number_of_liter = amount/price_per_liter
    return number_of_liter


def get_fuel_by_number_of_liter(number_of_liter,amount_per_liter):
    amount = number_of_liter * amount_per_liter
    return amount


def calc_total_cost_with_liter(liter_amount,cost_per_liter):
    total_cost = liter_amount * cost_per_liter
    return total_cost

def calc_total_cost_with_amount(amount,cost_per_liter):
    total_cost = amount /cost_per_liter
    return total_cost


def get_all_transaction_history(product,amount,liter):
    transaction = {
        "product": product,
        "amount": amount,
        "liter": liter,

    }
    all_transactions.append(transaction)
    return all_transactions


def get_receipt(product, amount, liter):
    receipt = f"""\nCustomers Transaction Receipt\n===========================\n= Product: {product}\n= Amount: {amount}\n= Liter: {liter}L\n= Date: {date.today()}\nThanks for your patronage\n==========================\nSaving Transaction History....."""
    return receipt


def get_receipt_gas(product, amount, liter,t_date):
    receipt = f"""\nCustomers Transaction Receipt\n===========================\n= Product: {product}\n= Amount: {amount}\n= KG: {liter}\n= Date: {date.today()}\nThanks for your patronage\n===========================\nSaving Transaction History....."""
    return receipt