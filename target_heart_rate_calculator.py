print("Target heart rate calculator")

age = int(input("enter age: "))

max_heart_rate = 220 - age

target_heart_rate = 50 - (max_heart_rate * 0.85)

print("Maximum heart rate of the user is: ", max_heart_rate)

print("Target heart rate of user is: ", target_heart_rate)
