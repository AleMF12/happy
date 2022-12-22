#Here the variables are defined as score1, score2, score3 and score4.
# The user is asked to input the 4 score values .
score1 = input("Score 1= ")
score2 = input("Score 2= ")
score3 = input("Score 3= ")
score4 = input("Score 4= ")

### YOUR CODE STARTS HERE
#Now I created a list of integers. First to use the value of scores I had
#to covert the variables using 'int' function
list_scores = list((int(score1), int(score2), int(score3), int(score4)))

#I used sort function to organize them from the lowest to the higgest value.
list_scores.sort()

#I pop the lowest value and wich is the first value with index 0
list_scores.pop(0)

#I use print function to display the average. To find the average I did something that
#I did in the previos assigment to sum up first all the values and then divided it to the number of them.
print((sum(list_scores))/(len(list_scores)))

### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
In this code I basically created a list asking the user to enter 4 scores, then it will drop the lowest score.
For that first I used sort to organized the values from the lowest to highest finally I found the average
using sum and len to later use print function to display the average on the screen.
### YOUR EXPLANATION ENDS HERE
"""