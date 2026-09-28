print("Bmi category ")

weight = int(input("enter weight: "))

height = int(input("enter weight: "))

bmi = weight/(height * height)

if 0 <= bmi <= 18.5:
    print("underweight")
    
if 18.6 <= bmi <= 24.9:
    print("normal")
    
if 25 <= bmi <= 29.9:
    print("overweight")
    
if 30<= bmi > 31:
    print("obese")
print("bmi is: ",bmi)  
    

