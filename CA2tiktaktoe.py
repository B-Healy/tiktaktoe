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
