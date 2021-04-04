# set up board 
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' ',}


#print out the board 
def print_board(board):
    print(board[1]+ '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4]+ '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7]+ '|' + board[8] + '|' + board[9])
    print("\n")
    
print_board(board)

#create a function to check if the space is free 
def space_free(position):
    #if position is empty return True 
    if(board[position]== " "):
        return True
    #if the position isnt " " return False    
    else:
        return False    

# define check for a tie 
def check_tie():
    for key in board.keys():
        #if there is anavalible space return False
        if board[key] == ' ':
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

#Create a function to insert letter(X or O)   
def inseart_letter(letter,position):
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
        position = int(input("Enter new possition to continue:")) 
        insert_letter(letter,position)
        return   

player = '0'
AI = 'X'
#define the players move 
def player_move():
    #takes position of player and converts it to an integer
    position = int(input("Enter the position you want to play 'O':"))
    insert_letter(player, position)
    return

#define the AI move 
def AI_move():
    #takes position of AI and converts it to an integer
    position = int(input("Enter the position you want to play 'X':"))
    insert_letter(AI, position)
    return
