from datetime import datetime

def calculate_item_total(price,quantity):
    if price < 1:
        return
       
    return price * quantity
    
def get_discount(subtotal,discount_rate):
    return subtotal * (discount_rate/100)
    
def calculate_vat(subtotal,discount_amount,vat_rate):
    return (subtotal - discount_amount) * (vat_rate / 100)
    

cashier_name = input("input cashier_name: ")
customer_name = input("input customer_name: ")
product_name = "No" 

items_bought = []
subtotal = 0.0

print("input items bought or input 'yes' to stop")

while product_name.lower() != "yes":
    product_name = input("what did customer bought: ")
    if product_name.lower() == "yes":
        break
    
    quantity = int(input("How many pieces: "))
    price =float(input("Enter unit price of the item: "))
    
    item_total = calculate_item_total(price,quantity)
    subtotal += item_total
    
    items_bought.append({"name": product_name,"qty": quantity, "price": price, "total": item_total}) 
          
    print("-" * 40)
        
        
discount_rate = float(input("Enter discount e.g 10 for 10%"))
vat_rate = 17.50

discount_amount = get_discount(subtotal,discount_rate)
vat_amount = calculate_vat(subtotal, discount_amount, vat_rate)
final_total = subtotal + vat_amount - discount_amount

current_time = datetime.now().strftime("%d-%b-%y %I:%M:%S %p")


print("=" * 50)
print("\t\tWELCOME TO SEMICOLON STORE \n MAIN BRANCH\n LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\n TEL: 03293828343\n Cashier's name: ", cashier_name, "\n Customer name: ", customer_name)
print(f"Date : {current_time}")

print("=" * 50)
print(f"{'ITEM' :<15}{'QTY' :<8}{'PRICE' :<10}{'TOTAL(NGN)' :<12} ")
print("-" * 50)

for item in items_bought:
    print(f"{item['name'] :<15}{item['qty'] :<8}{item['price']:<10.2f}{item['total'] :<12.2f}")

print("-" * 50)
print(f"Subtotal:       NGN {subtotal:.2f}")
print(f"Discount:       NGN {discount_amount:.2f}")
print(f"VAT({vat_rate}%):NGN {vat_amount:.2f}")
print("-" * 50 )
print(f"Grand Total:       NGN {final_total:.2f}")
print("THIS IS NOT A RECEIPT KINDLY PAY", final_total)


amount_paid = float(input("Enter how much customer gave you"))
balance = amount_paid - final_total


print("=" * 50)
print("\t\tWELCOME TO SEMICOLON STORE \n MAIN BRANCH\n LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\n TEL: 03293828343\n Cashier's name: ", cashier_name, "\n Customer name: ", customer_name)
print(f"Date : {current_time}")

print("=" * 50)
print(f"{'ITEM' :<15}{'QTY' :<8}{'PRICE' :<10}{'TOTAL(NGN)' :<12} ")
print("-" * 50)

for item in items_bought:
    print(f"{item['name'] :<15}{item['qty'] :<8}{item['price']:<10.2f}{item['total'] :<12.2f}")

print("-" * 50)
print(f"Subtotal:       NGN {subtotal:.2f}")
print(f"Discount:       NGN {discount_amount:.2f}")
print(f"VAT({vat_rate}%):NGN {vat_amount:.2f}")
print("=" * 50 )
print(f"{'Bill Total:' :>38}{final_total :>15.2f}")
print(f"{'Amount Paid:' :>38}{amount_paid :>15.2f}")
print(f"{'Balance:' :>38}{balance :>15.2f}")
print(f"{'THANK YOU FOR YOUR PATRONAGE'}")
print("=" * 50 )
























