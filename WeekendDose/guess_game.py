print("Guess game")

number = int(input("Guess between 1 and 100 to play: "))

while number > 0:
    if 0<= number <= 50:
        print("guess to low")
        number = int(input("Guess between 1 and 100 to play: "))    
    elif 52<= number <= 100:
        print("guess to high")
        number = int(input("Guess between 1 and 100 to play: "))    
    elif number == 51:
        print("you win")
        number = int(input("Guess between 1 and 100 to play: "))    
    

