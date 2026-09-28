print("Promo! Promo!! Promo!!!")
print()

def promo_code_checker():
    item_name = input("enter item name: ")
    original_price = int(input("enter original price of item: "))
    promo_code = input("enter promo code: ").upper()

    if promo_code == "SAVE10":
        print(original_price - original_price * 0.1)

    elif promo_code == "HALFOFF":
        print(original_price - original_price * 0.5)
    else:
        print(original_price)

promo_code_checker()
