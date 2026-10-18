rows = 6
cols = 7
empty = 0
human = 1
ai = 2

def create_board():
    board = []
    for i in range (rows):
        empty_row =[]     #create empty row to add after finshing column
        for j in range (cols):
            empty_row.append(empty)    #adding zeros to empty row
        board.append(empty_row)     #add new row
    return board

def display_board(board):
    for row in board:  #goes through each item(row) in board
        print(*row)

def drop_piece(board, col, player):
    for row in board[::-1]:   #search starting from bottom row
        if row[col] == empty:
           row[col] = player
           return True
    return False

def get_valid_moves(board):
    valid = []
    for col in range (len(board[0])):  #checks if top slot is open
        if board[0][col] == empty:
           valid.append(col)
    return valid  #returns list of valid cols


def check_winner(board, player):
    #horizontal dectection
    for row in range(rows):
        for col in range (cols-3):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == player:
               return True

    #vertical detection:
    for col in range(cols):
        for row in range (rows-3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == player:
               return True

    #diagonal(down) dectection
    for row in range(rows-3):
        for col in range (cols-3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == player:
               return True



    #diagonal(up) dectection
    for row in range(3,rows):
        for col in range (cols-3):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == player:
               return True


    return False
