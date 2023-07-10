#TicTacToe Console  Game 
"""
TicTacToe Console Game
Implimented With the help some online tutorial
Game Rules : 
@ This game requires two players
1.The Game Board like this 
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
2. There are 9 spaces indicates 1-9 numbers .
3. First player has to select the number between 1 to 9 in player given place "X" will be placed
@Example:
Player - 1 :- Enter position that want  between (1-9) : 2
- | X | -
- | - | -
- | - | -
The game board look like this
After Player 1 game it asks for second player postion like
For the second player given position "O" will be placed
player-2 :- Enter position that want  between (1-9) : 1
O | X | -
- | - | -
- | - | -
4. If same symbol can be fill vetically or Horizontally or Diagonally The respected player will win the game
    if
O | X | -
- | X | -
- | X | -    

in this above senario Player 1 won the game !
"""

import random

board = ["-" for i in range(9)] #Here we taking list of empty spaces in length of 9

def gameBoard(board):
    #Printing Game board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print()
    print(board[3] + " | " + board[4] + " | " + board[5])
    print()
    print(board[6] + " | " + board[7] + " | " + board[8])
    return 

def fillMove(letter,position):
    # board[move-1] = the respective Symbol
    board[position-1] = letter

def isAvailable(position):
    #In this function we check board[move - 1] is an empty space so we compare position with "-" if true it retuns True
    #else False
    #Here board is the list which we declare at above
    return board[position-1] == '-'
    
def isBoardFull(board):
    # Here we count no.of  empty spaces in our board empty space represents this : "-"
    #So we count them if the count is greater than 0 it returns False else returns True 
    if board.count('-') > 0:
        return False
    else:
        return True

def isWinner(board,letter):
    #Here we check any symbol is repeated vertically or Horizontally or Diagonally
    return (board[0] == board[1] == board[2] == letter) or (board[3] == board[4] == board[5] == letter) or(board[6] == board[7] == board[8] == letter) or (board[0] == board[4] == board[8] == letter) or (board[2] == board[4] == board[6] == letter) or (board[0] == board[3] == board[6] == letter) or (board[1] == board[4] == board[7] == letter) or (board[5] == board[2] == board[8] == letter)
    
def player():
    # we are taking while infinite loop because we don't know if player enter any input other than 
    #Given numbers it has to ask enter a valid input  
    while True:
        move = input("Player - 1 :- Enter position that want  between (1-9) : ")
        if move.isnumeric(): # we check given input is an integer if True
            move = int(move) #  we convert move to integer
            if move > 0 and move <= 9: # we check if the given move is in given range if True 
                if isAvailable(move): #We check given move is empty in Our game board so we call isAvailable(move) function
                    fillMove('X',move) # If the move is avialable we fill the board with the respective Symbol 
                                        #To do that we call fillMove(X,move) function (letter = X position = move)
                    gameBoard(board)    #   We print the board again
                    break
                else:
                    #If the given postion is not available
                    print("This position is not available!")
            else:
                #if the given move is out of range
                print("Please enter a number between given range !")
        else:
            #If player enters input other than integer
            print("Enter a valid input!")

def player2():
    #Player 2 is same as player 1
    while True:
        move = input("player-2 :- Enter position that want  between (1-9) : ")
        if move.isnumeric():
            move = int(move)
            if move > 0 and move <= 9:
                if isAvailable(move):
                    fillMove('O',move)
                    gameBoard(board)
                    break
                else:
                    print("This position is not available!")
            else:
                print("Please enter a number between given range !")
        else:
            print("Enter a valid input!")

def start():
    # This is the starting point of the Program
    print("Welcome to Tic Toc Toe console Game")
    gameBoard(board) # We are printing the game board here for that we call gameBoard() function
    # To check if the game board is full we call isBoardFull() function
    while not isBoardFull(board): 
        player() # We call player 1 function player()
        if isWinner(board,'X'): #After inerst the move in respective place and the symbol we check isWinner() funnction
                                #If True we stop the game
            print("Player 1 won this game!")
            break
        player2() # After player 1 game We call Player2 Function
        if isWinner(board,'O'): #Again we check isWinner() function if it returns true we stop the game
            print("Player 2 won this gamee!")
            break
    else:
        #If no Player is not satisfying the isWinner() function we declare it as draw
        print("Game tie!")
        

start()




