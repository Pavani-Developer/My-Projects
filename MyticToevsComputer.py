import random

board = ["-" for i in range(9)]

def gameBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print()
    print(board[3] + " | " + board[4] + " | " + board[5])
    print()
    print(board[6] + " | " + board[7] + " | " + board[8])
    return 

def fillMove(letter,position):
    board[position-1] = letter

def isAvailable(position):
    return board[position-1] == '-'
    
def isBoardFull(board):
    if board.count('-') > 0:
        return False
    else:
        return True

def isWinner(board,letter):
    return (board[0] == board[1] == board[2] == letter) or (board[3] == board[4] == board[5] == letter) or(board[6] == board[7] == board[8] == letter) or (board[0] == board[4] == board[8] == letter) or (board[2] == board[4] == board[6] == letter) or (board[0] == board[3] == board[6] == letter) or (board[1] == board[4] == board[7] == letter) or (board[5] == board[2] == board[8] == letter)
    
def player():
    while True:
        move = input("Enter position that want  between (1-9) : ")
        if move.isnumeric():
            move = int(move)
            if move > 0 and move <= 9:
                if isAvailable(move):
                    fillMove('X',move)
                    gameBoard(board)
                    break
                else:
                    print("This position is not available!")
            else:
                print("Please enter a number between given range !")
        else:
            print("Enter a valid input!")

def computerPlayer():
    corners = [1,3,7,9,2,4,6,8,5]
    #edges = [2,4,6,8]
    while True:
        if len(corners) > 0:
            move = random.choice(corners)
            corners.remove(move)
            if isAvailable(move):
                fillMove('O',move)
                gameBoard(board)
                break
                
            """elif len(edges) > 0:
            move = random.choice(edges)
            edges.remove(move)
            if isAvailable(move):
                fillMove('O',move)
                gameBoard(board)"""
            """else:
            move = 5
            if isAvailable(move):
                fillMove("O",move)
                gameBoard(board)"""

def start():
    print("Welcome to Tic Toc Toe console Game")
    gameBoard(board)
    while not isBoardFull(board):
        player()
        if isWinner(board,'X'):
            print("X player won this game!")
            break
        computerPlayer()
        if isWinner(board,'O'):
            print("Computer won this game!")
            break
    else:
        print("Game tie!")
        

start()




