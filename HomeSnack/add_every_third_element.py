print("add every third element")

def add_everythird_element(numbers):
    
    sum_result = 0
    
    for position in range(2,len(numbers),3):
        
        sum_result += numbers[position]
        
    return sum_result
    
list_sample = list(range(10))

sum_result = add_everythird_element(list_sample)

print(sum_result)
    

