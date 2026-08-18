print("Add elements")

def get_sum(numbers):

    total = 0
    
    for position in range(len(numbers)):
        
        total += numbers[position]
        
    return total

int_numbers = list(range(1,16))

sum_total = get_sum(int_numbers)

print(sum_total)
