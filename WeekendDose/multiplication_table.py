print("Multiplication Table" )

digit1 = int(input("Enter number: "))
digit2 = int(input("Enter number: "))

for akojopo1 in range(1,digit1 + 1):
    for akojopo2 in range(1,digit2 + 1):
        print(akojopo2, "X", akojopo1, "=", akojopo2 * akojopo1, end="\t")
    print()
            
