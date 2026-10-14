

def display_board(board):
 for i in range (0,9,3):
   print(board[i], board[i+1],  board[i+2],  "    ", i, i+1, i+2)
 print()

def find_winner(board):
 wins = [ (0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8),(0,4,8), (2, 4, 6) ]

 for i,j,k in wins:
    if board[i] != "." and board[i] == board[j] == board[k]:
       return board[i]

 if "." not in board:
      return "Draw"

 return None

# Alpha-beta pruning added to minimax
# alpha = best score the AI (maximizer) can guarantee so far — starts at -10
# beta  = best score the opponent (minimizer) can guarantee so far — starts at 10
# If beta <= alpha, we prune (stop early) because the other player would never let us reach this branch anyway
def minimax(board, maximize, ai, alpha=-10, beta=10):
   winner = find_winner(board)

   if winner is not None:
     if winner == ai:
       return 1
     elif winner == "Draw":
       return 0
     else:
       return -1

   person = "O" if ai == "X" else "X"

   if maximize:
     best_result = -10
     for i in range(9):
       if board[i]  == ".":
          new_board = board[:i] + ai + board[i+1:]
          result = minimax(new_board, False, ai, alpha, beta)
          best_result = max(best_result, result)
          alpha = max(alpha, best_result)  # update alpha
          if beta <= alpha:                # PRUNE — minimizer above won't allow this
            break
     return best_result

   else:
     best_result = 10
     for i in range(9):
       if board[i] == ".":
         new_board = board[:i] + person + board[i+1:]
         result = minimax(new_board, True, ai, alpha, beta)
         best_result = min(best_result, result)
         beta = min(beta, best_result)   # update beta
         if beta <= alpha:               # PRUNE — maximizer above won't allow this
           break
     return best_result

def ai_move(board, ai):
   moves = []

   for i in range(9):
       if board[i] == ".":
         new_board = board[:i] + ai + board[i+1:]
         score = minimax(new_board, False, ai, alpha=-10, beta=10)

         if score == 1:
          result = "Winning"
         elif score == 0:
           result = "Tying"
         else:
           result = "Losing"
         moves.append((i, score, result))

   for move, score, result in moves:
       print(f"Moving at {move} results in a {result}.")
   winning = [a for a in moves if a[1] == 1]
   tying = [a for a in moves if a[1] == 0]
   losing = [a for a in moves if a[1] == -1]

   if winning:
     space = winning[0][0]
   elif tying:
       space = tying[0][0]
   else:
      space = losing[0][0]

   print(f"\nI choose space {space}.\n")
   board = board[:space] + ai + board[space+1:]
   return board


def human_move(board, human):
    valid_spaces =  [i for i in range(9) if board[i] == "."]
    print("You can move to any of these space:", ", ".join(map(str, valid_spaces)))

    while True:
     choice = input("Your choice? ").strip()
     if choice.isdigit() and int(choice) in valid_spaces:
        move = int(choice)
        board = board[:move] + human + board[move+1:]
        return board
     print("Not valid move. Try again")

def main():
   board = input("Enter board state of 9 character(. , X, O) Leave blank for empty board ")
   if board == "":
      board = "........."
   if len(board) !=9 or any(char not in "XO." for char in board):
      print("Not valid board.")
      return

   while True:
     human = input("Wanna be X or O? ").strip().upper()
     if human in ["X", "O"]:
        break
     print("Make sure to enter X or O")

   ai = "X" if human == "O" else "O"
   print("\nStarting board")
   display_board(board)

   while find_winner(board) is None:
       num_x = board.count("X")
       num_o = board.count("O")
       current = "X" if num_x == num_o else "O"

       print(f" Current player: {current}")

       if current == human:
          board = human_move(board, human)
       else:
          board = ai_move(board, ai)

       print("\nBoard after move")
       display_board(board)

   winner = find_winner(board)
   if winner == ai:
      print("I win!")
   elif winner == human:
      print("You win!")
   else:
      print("We tied!")



if __name__== "__main__":
 main()
