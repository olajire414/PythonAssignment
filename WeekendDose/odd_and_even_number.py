print("Print odd or even number between 1 and 100")
odd_counter = 0
even_counter = 0
for number in range(1,101):
    if number % 2 ==1:
        odd_counter += 1
        
    if number % 2 == 0:
        even_counter += 1           

print("number of odd numbers are: ",odd_counter)
print("number of even numbers are: ",even_counter)
