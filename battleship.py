from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
for turn in range(4):
    throw = str(turn + 1)
    print "Turn " + throw
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        throw = str(turn + 1)
        print "Turn " + throw
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if turn == 2:
            throw = str(turn + 1)
            print "Turn " + throw
            print "Game Over"
            break
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            throw = str(turn + 1)
            print "Turn " + throw
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            throw = str(turn + 1)
            print "Turn " + throw
        else:
            print "You missed my battleship!"                
            board[guess_row][guess_col] = "X"
            throw = str(turn + 1)
            print "Turn " + throw
            print_board(board)