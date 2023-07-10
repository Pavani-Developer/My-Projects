import random
print("Welcome to Rock Paper Scissor Console Game ")
print('Enter any of one word in given words "Rock","rock","paper","Paper","Scissor","scissor" ')
while True:
    game_elements = ["Rock","rock","paper","Paper","Scissor","scissor"]
    computer_guess = random.choice(game_elements)
    player = input("Enter your Guess : ")
    print(f"Your guess is: {player}")
    print(f"Commputer guess is:{computer_guess} ")
        
    
    if computer_guess == "Rock" or computer_guess == "rock":
        if player == "Paper" or player == "paper":
            print("Congrats! You won the game")
        
        if player == "Scissor" or player == "scissor":
            print("Computer won the game ! Better luck next time Have a Nice day :)")
        
        if computer_guess == "Rock" or computer_guess == "rock" and player == "rock" or player == "Rock":    
            print("Oh No Tie! Play again")
        
 
            
    elif computer_guess == "Paper" or computer_guess == "paper":
        if player == "scissor" or player == "Scissor":
            print("Congrats! You won the game")
        
        if player == "Rock" or player == "rock":
            print("Computer won the game ! Better luck next time Have a Nice day :)")
        
        if computer_guess == "Paper" or computer_guess == "paper" and player == "Paper" or player == "paper":
            print("Oh No Tie! Play again")
        
            
    elif computer_guess == "Scissor" or computer_guess == "scissor":
        if player == "Rock" or player == "rock":
            print("Congrats! You won the game")
        
        if player == "Paper" or player == "paper":
            print("Computer won the game ! Better luck next time Have a Nice day :)")
        
        if computer_guess == "Scissor" or computer_guess == "scissor" and player == "scissor" or player == "Scissor":    
            print("Oh No Tie! Play again")
        
    user_choice = input("Do you want play again (Y/N): ")
    if user_choice == "N":
        print("Thank you for playing :)")
        break
        
