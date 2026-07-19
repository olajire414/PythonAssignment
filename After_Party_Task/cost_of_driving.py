# print label
#collect input for each parameter
# write formula
#print outcomes

print(" input the values to get your driving cost ")

driving_distance = float(input("driving_distance : "))

miles_per_galon= float(input("miles_per_galon: "))

price_per_galon = float(input("price_per_galon: "))

driving_cost = (driving_distance * price_per_galon)/miles_per_galon


print("Driving cost is: ",driving_cost )
