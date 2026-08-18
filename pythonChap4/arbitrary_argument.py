
#4.13
print("Arbitrary Argument")

print()

def get_product_of_number(*numbers):
    sum_of_number = 0
    for number in numbers:
        sum_of_number += number
    
    return sum_of_number
    
print( "Sum: ", get_product_of_number(1,3,3,3,5,5,5,5,5,5))
    
