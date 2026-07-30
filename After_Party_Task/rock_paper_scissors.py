#collect input from player 1 & player 2
#invoke if statement
#compare  player 1 & 2 inputs
#print outcomes


print(" enter one of these: rock,paper or scissors ")

player1 = input("enter one of the  options: ")

player2 = input("enter one of the options: ")

if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins")
    
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins")

elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins")

elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins")

elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins")

elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins")
    
else:
    print("Ties")
        
    

