"""
Tic Tac Toe Game

Human plays as X.
Computer plays as O.

The computer automatically selects
an empty position.
"""

import random

# Game board
board = [" " for i in range(9)]
def display_board():
    
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):

    win_positions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for position in win_positions:

        if (
            board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player
        ):
            return True

    return False

def check_draw():
    
    return " " not in board

def computer_move():
    
    empty_positions = []

    for i in range(9):

        if board[i] == " ":
            empty_positions.append(i)


    position = random.choice(empty_positions)

    board[position] = "O"

    print("Computer selected position:", position + 1)

def human_move():

    while True:

        position = int(input("Enter your position (1-9): "))

        index = position - 1


        if index < 0 or index > 8:
            print("Invalid position")

        elif board[index] != " ":
            print("Position already used")

        else:
            board[index] = "X"
            break

def play_game():
    
    while True:

        # Human turn
        display_board()

        print("Your Turn (X)")
        human_move()


        if check_winner("X"):
            display_board()
            print("You Win 🎉")
            break


        if check_draw():
            display_board()
            print("Game Draw 🤝")
            break

        # Computer turn
        computer_move()


        if check_winner("O"):
            display_board()
            print("Computer Wins 🤖")
            break


        if check_draw():
            display_board()
            print("Game Draw 🤝")
            break
if __name__ == "__main__":
    play_game()