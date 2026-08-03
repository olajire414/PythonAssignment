print("Temperature Adviser")
print()

def temperature_checker():
    temp_value = int(input("enter temperature value: "))
    temp_unit = input("enter unit celcius'C' or fahrenheit'F': ").upper()
    

    if  temp_unit == "F":
        celcius = (temp_value - 32) *5/9

        print("Temperature in celcius is: ", celcius)

    elif celcius < 32:
        print("The temprature is below normal 'Too much cold today'") 

    elif celcius > 32:
        print("The temp is above normal 'Too much heat today'")            
        
    elif temp_unit == "C":
        fahrenheit = (temp_value *9/5) + 32
        print("Temperature in fahrenheit is: ",fahrenheit )
    
    elif  fahrenheit > 32:
        print("The temprature is above normal 'Too much heat today'")
    elif fahrenheit < 32:
        print("The temprature is below normal 'Too much cold today'")  
           
    else:
        print("invalid input")

temperature_checker()
