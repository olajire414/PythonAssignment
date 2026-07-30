print(" enter 'velocity' in m/s and 'acceleration' in m/s2  ")

velocity = float(input("enter velocity : "))

acceleration = float(input("enter acceleration : "))

runway_length = (velocity **2)/ (2 * acceleration)

print("runway length is: ",runway_length)

