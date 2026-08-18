def get_odd_sum(numbers):

    print("Sum of element at odd position in a list")
    
    total = 0
       
    for digits in range(2,len(numbers),2):
    
            total += numbers[digits]
    return total
    


room_number = list(range(1,10))

print(get_odd_sum(room_number))

print(room_number)



