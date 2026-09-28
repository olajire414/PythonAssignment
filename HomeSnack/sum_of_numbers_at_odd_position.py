def get_even_sum(numbers):

    print("Sum of element at even position in a list")
    
    sum_total = 0
       
    for digits in range(0,len(numbers),3):
    
            sum_total += numbers[digits]
    return sum_total
    


room_number = list(range(10))

print(get_even_sum(room_number))

print(room_number)



