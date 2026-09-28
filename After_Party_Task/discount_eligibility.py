#collect input of the total bill
#collect input of is a member
#invoke if statement to compare the parameters 
#(membership and price) and set conditions
#calculate the percentage dicount minus it from total bill

print("Discount Eligibility")

total_bill = int(input("enter total bill: "))

is_member = input("a member? yes/no: ")

if total_bill >=1000 and is_member == "yes":
    print("10% off, Total bill is: ",total_bill -(total_bill * 0.1))
    
elif total_bill >=1000 and is_member == "no":
    print("5% off, Total bill is: ",total_bill - (total_bill * 0.5))
    
else: 
    print("No discount, your bill is: ",total_bill)
