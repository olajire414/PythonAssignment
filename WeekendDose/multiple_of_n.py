print("Multiple of n")

digit = int(input("enter number: "))
for number in range(1,101):
    if number % digit == 0:
        print(number, end=" ")
