

def guess_game():
    import random
    print("Guess a number between 1 and 1000 to play")

    guess_number = int(input("Enter number between 1 and 1000: "))

    play = True
    counter = 0
    random_number = random.randint(1,1000)

    while play:
        if guess_number < random_number:
            print("Guess too low try again!!!")
            guess_number = int(input("Enter number between 1 and 1000: "))
            counter += 1
        elif guess_number > random_number:
            print("Guess too high try again!!!")
            guess_number = int(input("Enter number between 1 and 1000: "))
            counter += 1
        elif  guess_number == random_number:
            print("congratulation, 'you guess the number' ")
            print("'Play again' ")
            guess_number = int(input("Enter number between 1 and 1000: "))
            counter += 1
        else:
            print("Dont be a loser") 
            guess_number = int(input("Enter number between 1 and 1000: "))
            counter += 1    

        if counter > 10:
            print(""" "You should be able to do better!" Why should it take  more   than 10 guesses?"  """)  
            
            
guess_game()            
             
