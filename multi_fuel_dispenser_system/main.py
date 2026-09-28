from datetime import date
import fuel_dispenser_app

transaction_history = []


print("*" * 50)
print("Welcome To Sunshine Filling Station")
print("*" * 50)

main_menu_choice = """
1. Buy Petroleum
2. Show Transaction History
0. Exit
"""
print(main_menu_choice)
print()

main_menu = int(input("Choose your choice: "))
while main_menu != 0:
    if main_menu < 0 or main_menu > 2:
        print("Please enter a valid choice")
        main_menu = int(input("Choose your choice: "))
    match main_menu:
        case 1:
            print(fuel_dispenser_app.display_board())

            choice = int(input("Choose fuel type/Yes to quit app: "))
            if choice < 0 or choice > 5:
                print("Please enter a valid choice")
            while choice != 0:
                match choice:
                    case 1:
                        cost_per_liter = 650
                        product = "Diesel"
                        user_choice = input("liter or amount: ").lower()
                        if user_choice == "liter":
                            number_of_liters = float(input("How many liter of petrol are you buying(650/L): "))
                            if number_of_liters < 0 or number_of_liters > 50:
                                print("Please enter between 1 and 50")
                            amount = fuel_dispenser_app.calc_total_cost_with_liter(number_of_liters, cost_per_liter)


                            transaction_history.append(
                                fuel_dispenser_app.get_all_transaction_history(product, amount, number_of_liters))
                            print(fuel_dispenser_app.get_receipt(product, amount, number_of_liters))

                        elif user_choice == "amount":
                            amount = float(input("How much petrol are you buying(650/L): "))
                            if amount < 0:
                                print("Please enter a positive amount")
                            number_of_liters = fuel_dispenser_app.get_fuel_by_amount(amount, cost_per_liter)


                            transaction_history.append(
                                fuel_dispenser_app.get_all_transaction_history(product, amount, number_of_liters))
                            print(fuel_dispenser_app.get_receipt(product, amount, number_of_liters))

                        elif user_choice != "liter" and user_choice != "amount":
                            print("Please enter either liter or amount")

                        else:
                            print("invalid input")
                        break

                    case 2:
                        cost_per_liter = 720
                        product = "Diesel"
                        user_choice = input("liter or amount: ").lower()
                        if user_choice == "liter":
                            number_of_liters = float(input("How many liter of diesel are you buying(650/L): "))
                            if number_of_liters < 0 or number_of_liters > 50:
                                print("Please enter between 1 and 50")
                            amount = fuel_dispenser_app.calc_total_cost_with_liter(number_of_liters, cost_per_liter)


                            transaction_history.append(
                                fuel_dispenser_app.get_all_transaction_history(product, amount, number_of_liters))
                            print(fuel_dispenser_app.get_receipt(product, amount, number_of_liters))


                        elif user_choice == "amount":
                            amount = float(input("How much diesel are you buying(720/L): "))
                            if amount < 0:
                                print("Please enter a positive amount")
                            number_of_liters = fuel_dispenser_app.get_fuel_by_amount(amount, cost_per_liter)


                            transaction_history.append(
                                fuel_dispenser_app.get_all_transaction_history(product, amount, number_of_liters))
                            print(fuel_dispenser_app.get_receipt(product, amount, number_of_liters))

                        elif user_choice != "liter" and user_choice != "amount":
                            print("Please enter either liter or amount")

                        else:
                            print("invalid input")
                        break

                    case 3:
                        cost_per_liter = 550
                        product = "Kerosene"
                        user_choice = input("liter or amount: ").lower()
                        if user_choice == "liter":
                            number_of_liters = float(input("How many liter of kerosene are you buying(550/L): "))
                            if number_of_liters < 0 or number_of_liters > 50:
                                print("Please enter between 1 and 50")
                            amount = fuel_dispenser_app.calc_total_cost_with_liter(number_of_liters, cost_per_liter)


                            transaction_history.append(
                                fuel_dispenser_app.get_all_transaction_history(product, amount, number_of_liters))
                            print(fuel_dispenser_app.get_receipt(product, amount, number_of_liters))


                        elif user_choice == "amount":
                            amount = float(input("How much kerosene are you buying(550/L): "))
                            if amount < 0:
                                print("Please enter a positive amount")
                            number_of_liters = fuel_dispenser_app.get_fuel_by_amount(amount, cost_per_liter)


                            transaction_history.append(
                                fuel_dispenser_app.get_all_transaction_history(product, amount, number_of_liters))
                            print(fuel_dispenser_app.get_receipt(product, amount, number_of_liters))

                        elif user_choice != "liter" and user_choice != "amount":
                            print("Please enter either liter or amount")

                        else:
                            print("invalid input")
                        break

                    case 4:
                        cost_per_liter = 480
                        product = "Gas"
                        user_choice = input("kg or amount: ").lower()
                        if user_choice == "kg":
                            number_of_kg = float(input("How many KG of gas are you buying(480/L): "))
                            if number_of_kg < 0 or number_of_kg > 50:
                                print("Please enter between 1 and 50")
                            amount = fuel_dispenser_app.calc_total_cost_with_liter(number_of_kg, cost_per_liter)


                            transaction_history.append(fuel_dispenser_app.get_all_transaction_history(product, amount, number_of_kg))
                            print(fuel_dispenser_app.get_receipt_gas(product, amount, number_of_kg, date.today()))


                        elif user_choice == "amount":
                            amount = float(input("How much gas are you buying(480/L): "))
                            if amount < 0:
                                print("Please enter a positive amount")
                            number_of_liters = fuel_dispenser_app.get_fuel_by_amount(amount, cost_per_liter)


                            transaction_history.append(
                                fuel_dispenser_app.get_all_transaction_history(product, amount, number_of_liters))
                            print(fuel_dispenser_app.get_receipt_gas(product, amount, number_of_liters, date.today()))

                        elif user_choice != "kg" and user_choice != "amount":
                            print("Please enter either liter or amount")

                        else:
                            print("invalid input")
                        break

                    case _:
                        print("invalid choice")
                        break

        case 2:

            print(transaction_history)
        case 0:
            print("Exiting...")
        case _:
            print("invalid input")


    print(main_menu_choice)
    main_menu = int(input("Choose your choice: "))
