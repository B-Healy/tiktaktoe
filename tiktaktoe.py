#create board 
#display board 
#play game function 
#change player turns 
#check win (columns, rows, diagonals )
#check draw 

#I"m going to use a list to create a board 
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

# define a function to display the baord 
def board_display():
    print("|---------------|")
    print("| Tik Tak Toe |")
    print("|---------------|")
    print("                 ")
    print("|    " + board[0][0] + " " + board[0][1] + " " + board[0][2]+ "    |")
    print("|    " + board[1][0] + " " + board[1][1] + " " + board[1][2]+ "    |")
    print("|    " + board[2][0] + " " + board[2][1] + " " + board[2][2]+ "    |")
    print("|---------------|")
    print()

    board_display()