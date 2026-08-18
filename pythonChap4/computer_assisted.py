
def multiplication():
    import random
    print(" Computer-Assisted learn Multiplication")
    print()
    play = True

    
    while play:
    
        random_number1 = random.randrange(1,10) 
        
        random_number2 = random.randrange(1,10) 
        
        print("How much is: ", random_number1 ,"times", random_number2)
        
        response = int( input("Enter your answer: "))
        
        correct_answer = random_number1 * random_number2
        
        if response == correct_answer:        
           print("Very Good")
           break
            
        elif response != correct_answer:
            
            print("No, try again ")
            print("How much is: ", random_number1 ,"times", random_number2)
        
            response = input("Enter your answer: ")
            
        else:
            ("invalid input")
            
            
       
        
            
    
                 
    #return
    
multiplication()
    

    
