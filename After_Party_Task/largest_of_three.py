

print(" Enter three integers ")

number1 = int(input("enter a number: "))

number2 = int(input("enter a number: "))

number3 = int(input("enter a number: "))

largest = number1

if number2 > largest:
    largest = number2

if number3 > largest:
    largest = number3
    
print("largest number is: ",largest)

