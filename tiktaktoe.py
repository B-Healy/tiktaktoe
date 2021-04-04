# NOT the tik tok toe for CA just another one i was trying 

#create board 
#display board 
#play game function 
#change player turns 
#check win (columns, rows, diagonals )
#check draw 

#I"m going to use a list to create a game board 
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#boolean if game is still running 
game_still_going = True

# winner or tie?  
winner = None

#who's turn
current_player = "X"

# define a function to display the baord 
def display_board():
    print(board[0]+ "|" + board[1] + "|" + board[2])
    print(board[3]+ "|" + board[4] + "|" + board[5])
    print(board[6]+ "|" + board[7] + "|" + board[8])

 #Create a function to play a game of tik tak toe 
def play_game():

    #display starting board
    display_board()
    #create loop while the game is still running
    while game_still_going:
        #handle a single turn of an arbitrary number 
        handle_turn(current_player)
        # Check if game is over
        check_if_game_over()
        # Flip to other player
        flip_player()

    #If the game has ended
    if winner == "X" or winner == "O":
         print(winner + " won.") 
    elif winner == None:
          print("Tie.")  

        
#define function to handle players turn 
def handle_turn(player):
   #print whos turn it is 
   print(player + "'s turn.")
   position = input("Choose a position from 1-9: ")

   valid = False
   while not valid:
      #if position is not from 1-9 ask for position again 
      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
         position = input("Choose position from 1-9:")
    
      #change position from string to integer and array starts at 0 so subtract 1 for corrct index
      position = int(position) - 1
   
      #ensure "X" or "O" cannnot be rewritten  
      if board[position] == "-":
         valid = True
      else:    
         print("Cant go there, pick an empty position")

   board[position] = player

   display_board()

#define function chech_if_game_over
def check_if_game_over():
    check_if_win()
    check_if_tie()

#difine wining states
def check_if_win():

    #set up global variables
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diaginals
    diaginals_winner = check_diaginals()

    #get winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diaginals_winner:
        winner = diaginals_winner
    else:
        winner = None

    return


def check_rows():
    #set up global variables
    global game_still_going
    #check if rows have all the same value except "-"
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any rows have the same value change game_still_going to false
    if row_1 or row_2 or row_3:
        game_still_going = False
    #returns winner either "X" or "O"    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]            
    return

def check_columns():
    #set up global variables
    global game_still_going
    #check if columns have all the same value except "-"
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if any columns have the same value change game_still_going to false
    if column_1 or column_2 or column_3:
        game_still_going = False
    #returns winner either "X" or "O"    
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]            
    return
    

def check_diaginals():
    #set up global variables
    global game_still_going
    #check if diaginals have all the same value except "-"
    diaginal_1 = board[0] == board[4] == board[8] != "-"
    diaginal_2 = board[2] == board[4] == board[6] != "-"
    #if any diaginals have the same value change game_still_going to false
    if diaginal_1 or diaginal_2: 
        game_still_going = False
    #returns winner either "X" or "O"    
    if diaginal_1:
        return board[0]
    elif diaginal_2:
        return board[2]     
    return

#difine function for a tie
def check_if_tie():
    #global variables needed 
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

#define function to alternate player turn 
def flip_player():
    #Global variable needed 
    global current_player
    # if current player is X then change it to O
    if current_player == "X":
      current_player = "O"
    #if current player is O change to X   
    elif current_player == "O":
        current_player = "X"
    return

# Play a game of tik tak toe 
play_game()    