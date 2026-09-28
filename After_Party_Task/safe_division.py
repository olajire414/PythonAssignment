#Question 1
#write the label that instruct the user to enter two numbers
#collect two number x & y
#invoke if statement to compare y
#print the output


print("Enter two numbers")

x = int(input("enter a number: "))

y = int(input("enter a number: "))

if y!=0:
    print("x/y is: ",x/y)

if y == 0:
    print("Cannot divide by zero")

