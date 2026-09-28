print("find the smallest in the list")

def get_smallest_element(numbers):

    smallest = numbers[0]

    for digits in range(len(numbers),0,1):
        
        if numbers[digits] < smallest:
            
            smallest = numbers[digits]
            
    return smallest
    
list_sample = list(range(1,10))

min1 = get_smallest_element(list_sample)

print(min1)




