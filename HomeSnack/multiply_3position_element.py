def get_product(numbers):

    print("Multiply  element at 3rd positions in a list")
    
    product = 1
       
    for digits in range(2,len(numbers),3):
    
            product *= numbers[digits]
    return product
    


room_number = list(range(10))

print(get_product(room_number))

print(room_number)


#1,2,3,4,5,6,7,8,9,7,8,7,6,43,3,2,3,2,2,1,3
