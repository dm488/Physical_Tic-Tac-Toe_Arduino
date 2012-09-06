# Tic Tac Toe

import random
import sys
import serial

def emptyBoard():
    return [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def getBoard(board):
    # Draw game board
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('---|---|---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')

def choose(board):
    Flag = True
    while Flag:
        print('Your move is?: \n')
        while 1:
            value = ser.read();
            place = value.decode("utf-8")
            if place in ['1','2','3','4','5','6','7','8','9']: break
        if place=='1' or place=='2' or place=='3' or place=='4' or place=='5' or place=='6' or place=='7' or place=='8' or place=='9':
            if board[int(place)]!=' ':
                print('That spot is taken already!')
                place=''
            else:
                Flag=False
    return int(place)

def isWinner(board):
    # Check for a winner at the end of each turn
    if board[7]!=' ' and board[7]==board[8] and board[8]==board[9]:
        return False
    elif board[4]!=' ' and board[4]==board[5] and board[5]==board[6]:
        return False
    elif board[1]!=' ' and board[1]==board[2] and board[2]==board[3]:
        return False
    elif board[7]!=' ' and board[7]==board[4] and board[4]==board[1]:
        return False
    elif board[8]!=' ' and board[8]==board[5] and board[5]==board[2]:
        return False
    elif board[9]!=' ' and board[9]==board[6] and board[6]==board[3]:
        return False
    elif board[7]!=' ' and board[7]==board[5] and board[5]==board[3]:
        return False
    elif board[9]!=' ' and board[9]==board[5] and board[5]==board[1]:
        return False
    else: return True

def gameloop():
    print('Welcome to Tic-Tac-Toe!')
    go = True
    board=emptyBoard()
    turn=1

    # Main game loop
    while go:

        # Show board
        getBoard(board)
        
        # Players make their moves
        print('Player 1, your move is?\n\n')
        placeX = choose(board)
        board[placeX]='X'

        # Refresh board
        getBoard(board)

        # Check for winner
        go = isWinner(board)
        if not go:
            endGame('Player 1')
        
        print('Player 2, your move is?\n\n')
        placeO = choose(board)
        board[placeO]='O'

        # Refresh board
        getBoard(board)

        # Check for winner
        go = isWinner(board)
        if not go:
            endGame('Player 2')

        turn=turn+1
        if turn==8:
            endgame('Nobody')

def endGame(winner):
    print('Congratulations ' + winner + ', you won!\n\nWould you like to play again?: \n')
    while 1:
        value = ser.read();
        rematch = value.decode("utf-8")
        if rematch in ['*','#']: break
    if rematch=='*':
        gameloop()
    else:
        print('Thanks for playing!\n')
        sys.exit(1)

#----------------------------------------------------

port="COM7"
ser = serial.Serial(port,9600)
value=0

# Start game
gameloop()
input("Press the enter key to exit.")
