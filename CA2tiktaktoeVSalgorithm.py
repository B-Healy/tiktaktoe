#print out the board 
def print_board(board):
    print(board[1]+ '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4]+ '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7]+ '|' + board[8] + '|' + board[9])
    print("\n")


#create a function to check if the space is free 
def space_free(position):
    #if position is empty return True 
    if board[position]== " ":
        return True
    #if the position isnt " " return False    
    else:
        return False    

# define check for a tie 
def check_tie():
    for key in board.keys():
        #if there is anavalible space return False
        if (board[key] == ' '):
            return False
    #otherwise return True        
    return True        


#define check for a win
def Check_win():
    #all conditions for win return true 
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True    
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    #if none of these conditions above are meet return False    
    else:
        return False            

#define check which mark won
def Check_which_mark_won(mark):
    # all the marks which win 
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True    
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    #if none of these conditions above are meet return False    
    else:
        return False                    

#Create a function to insert letter(X or O)   
def insert_letter(letter, position):
    #checks if space is free and if its free put in letter 
    if space_free(position):
        board[position] = letter
        print_board(board)

        #check for tie
        if(check_tie()):
            print("A tie!")
            exit() 

        #check for a win
        if Check_win():
            if letter == 'X':
                #if X wins(the ai) pint message 
                print("The AI wins!")
                exit()
            else:
                #otherwise human wins print 
                print("The impossible happened man defets AI.")
                exit()
        return                

    #if space isnt free 
    else:
        print("Cannot do that sorry :(")
        #take input and convert to integer 
        position = int(input("Enter new possition to continue: ")) 
        insert_letter(letter, position)
        return   


#define the players move 
def player_move():
    #takes position of player and converts it to an integer
    position = int(input("Enter the position you want to play 'O':"))
    insert_letter(player, position)
    return

#define the AI move 
def AI_move():
    #assign best score and best move 
    best_score = -800
    best_move = 0

    #go over each possible move 
    for key in board.keys():
        #if the board key is equal to an empty space we want to. play that move 
        if(board[key]== ' '):
            board[key]= AI
            #determine score 
            score = minimax(board, 0, False)
            #put the board empty again as we just want to get the score 
            board[key] = ' '
            # if the score is higher than the best score we change best score and best move 
            if(score > best_score):
                best_score = score
                best_move = key 

    insert_letter(AI , best_move)  
    return          

#define the minimax function 
def minimax(board, depth, is_maximizing):
    #terminal states  
    if (Check_which_mark_won(AI)):
        return 1

    elif (Check_which_mark_won(player)):
        return -1

    elif (check_tie()):
        return 0   

    #our AI find the best score untill terminal state is found 
    if (is_maximizing):
        best_score = -800
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = AI
                score = minimax(board, depth + 1 , False) 
                board[key] = ' ' 
                if (score > best_score):
                    best_score = score
        return best_score

    #enemy AI (minimising moment)    
    else:
        best_score = 800
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True) 
                board[key] = ' ' 
                if (score < best_score):
                    best_score = score
        return best_score


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

print_board(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
AI = 'X'

global first_AI_move
first_AI_move = True

# game to play AI first then player
while not Check_win():
    AI_move()
    player_move()