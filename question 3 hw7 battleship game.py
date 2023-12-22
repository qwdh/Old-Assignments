from random import randint

def printB(board):
    for row in board:
        print(" ".join(row))

def randRow(board):
    return randint(0, len(board) - 1)

def randCol(board):
    return randint(0, len(board[0]) - 1)

def playBs():
    board = []
    for _ in range(5):
        board.append(["O"] * 5)

    ship_row = randRow(board)
    ship_col = randCol(board)
    
    for turn in range(4):
        print(f"Turn {turn + 1}")
        printB(board)
        
        try:
            guessR = int(input("Guess Row (0-4): "))
            guessC = int(input("Guess Col (0-4): "))
            
            if guessR < 0 or guessR > 4 or guessC < 0 or guessC > 4:
                print("Oops, that's not even in the ocean.")
                continue
            
            if guessR == ship_row and guessC == ship_col:
                print("Congratulations! You sank my battleship!")
                break
            else:
                board[guessR][guessC] = "X"
                if turn == 3:
                    print("Game Over")
        except ValueError:
            print("Please enter a valid integer.")

playBs()
