print("find the largest in the list")

def get_largest_number(numbers):

    largest = numbers[0]

    for digits in range(len(numbers)):
        
        if numbers[digits] > largest:
            
            largest = numbers[digits]
            
    return largest
    
list_sample = list(range(99))

max1 = get_largest_number(list_sample)

print(max1)




    
    
