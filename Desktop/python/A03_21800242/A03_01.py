def read_test_data(filename):
    data = []
    with open(filename, "rt") as fin:
        lines = fin.read().strip().split("\n")
        for line in lines:
            row = line.split(" ")
            data.append(row)
    return data
    
def display_board(data):
    for row in data:
        print(" ".join(row))

tic_tac_toe = read_test_data(filename="test-data.txt")
print("== 3x3 Matrix (a list in a list) ==")
print(tic_tac_toe)
print()
print("== Tic-Tac-Toe Board ==")
display_board(tic_tac_toe)

### YOUR CODE STARTS HERE
#First I defined a variable called 'current player' and then with value X then I defined another
# variable called winner assigned the None value. After that I defined gameRunning variable and
# the value is True. Here we defined the initials values for the program.

currentPlayer = "X"
winner = None
gameRunning = True

# Here I defined a function called 'checkHorinzontle' in that function I used the conditionals to extract the
#winner in the  columns. The first if conditional is for the first column. The second elif conditional for the
#second column and the third for the third column. In the conditionals we are basically comparing every components
#of the column to find the winner.
def checkHorizontle(tic_tac_toe):
    global winner
    if tic_tac_toe[0][0] == tic_tac_toe[0][1] == tic_tac_toe[0][2] and tic_tac_toe[0][1] != "-":
        winner = tic_tac_toe[0][0]
        return True
    elif tic_tac_toe[1][0] == tic_tac_toe[1][1] == tic_tac_toe[1][2] and tic_tac_toe[1][0] != "-":
        winner = tic_tac_toe[1][0]
        return True
    elif tic_tac_toe[2][0] == tic_tac_toe[2][1] == tic_tac_toe[2][2] != "-":
        winner = tic_tac_toe[2][0]
        return True

#In this part the code of Check Row I used the conditional if to extract the winner in the rows.
#The first conditional 'if' was used for the first row, the second conditional 'elif' is for the second row
#and the last one for the last row. In general we are comparing all values in the row to check if they have
# same value. And after comparing if they have the same values that means the player wins.
def checkRow(tic_tac_toe):
    global winner
    if tic_tac_toe[0][0] == tic_tac_toe[1][0] == tic_tac_toe[2][0] and tic_tac_toe[0][0] != "-":
        winner = tic_tac_toe[0][0]
        return True
    elif tic_tac_toe[0][1] == tic_tac_toe[1][1] == tic_tac_toe[2][1] and tic_tac_toe[0][1] != "-":
        winner = tic_tac_toe[0][1]
        return True
    elif tic_tac_toe[0][2] == tic_tac_toe[1][2] == tic_tac_toe[2][2] and tic_tac_toe[0][2] != "-":
        winner = tic_tac_toe[0][2]
        return True
#In this part of the code of Check Diagonal I used the conditional if to extract the winner in the diagonal.
#The first conditional 'if' was used for the first diagonal, the second conditional 'elif' is for the second
#diagonal. In general we are comparing all values in the diagonlas  to check if they have
# same value. And after comparing, if they have the same values that means the player wins.

def checkDiagonal(tic_tac_toe):
    global winner
    if tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] and tic_tac_toe[0][0] != "-":
        winner = tic_tac_toe[0][0]
        return True
    elif tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0] and tic_tac_toe[0][2] != "-":
        winner = tic_tac_toe[0][2]
        return True
#In this part I am evaluating if there is a tie in the game. Then we are also putting the conditional game running to
# to false in order to stop the loop.
def checkTie(tic_tac_toe):
    global gameRunning
    if "-" not in tic_tac_toe:
        gameRunning = False

# This part is to create the function which checks the winner of the game by using if and elif conditional.
#It also display the 'Game Result' where it evaluates the result of the game in the horizontal and vertical

def checkWin():
    if checkDiagonal(tic_tac_toe) or checkHorizontle(tic_tac_toe) or checkRow(tic_tac_toe):
        print("== Game Result ==")
        print(f"{winner} won!")

    elif "-" in tic_tac_toe:
        print("There is an empty space")


# switch the player
#This part will switch the players X and O depending the value on the text file.
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
#Here it is just iterating over the all functions from checkWin function and then follow by checkTie with the
#argument Tic tac Toe file and finally switch player function.
# The purpose here is to call all the functions.
#to do their own roles.
while gameRunning:
    checkWin()
    checkTie(tic_tac_toe)
    switchPlayer()
### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
In this game we were asked to determine and display the winner of the Tic-Tac-Toe game. For that was very important 
to use conditionals (if and elif). Also for the game is basic and important to understand that there are  three 
options for player to win.
The player could be a winner in a column or in a row or in a diagonal. So for that we need to check on three of them. 
How we check is also important, in order to get the result we need to compare the componentes of a row, column or 
diagonal. If the three components are equal then we have a winner, the conditionals will help us to get the work 
done. Finally we can find a winner. The winner can be X or O. 
### YOUR EXPLANATION ENDS HERE
"""