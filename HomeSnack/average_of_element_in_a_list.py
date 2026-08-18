def get_average(numbers):

    print("Average of element in a list")
    
    average = 0
    sum_total = 0
       
    for digits in range(len(numbers)):
    
            sum_total += numbers[digits]
            average = sum_total/len(numbers)
    return average
    


room_number = list(range(10))

print(get_average(room_number))

print(room_number)



