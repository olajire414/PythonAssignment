    
    
def guess_game():  
    import random


    print("Guess a number between 1 and 1000 to play")
    random_number = random.randint(1,1000)

    guess_number = int(input("Enter number between 1 and 1000: "))
    play = True
    while play:
        
        if guess_number < random_number:
            print("Guess too low try again!!!")
            guess_number = int(input("Enter number between 1 and 1000: "))

        elif  guess_number > random_number:
            print("Guess too high try again!!!")
            guess_number = int(input("Enter number between 1 and 1000: "))

        elif  guess_number == random_number:
            print("congratulation, 'you guess the number' ")
            print(" 'Play again' ")
            guess_number = int(input("Enter number between 1 and 1000: "))

        else:
           
            print(" 'Play again' ")
            guess_number = int(input("Enter number between 1 and 1000: "))
    return;   
            
            
guess_game()          

