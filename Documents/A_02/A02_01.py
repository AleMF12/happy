#First step scores variable is assigned the value of the scores.
scores = [
    25, 32, 55, 0, 61,
    24, 89, 88, 53, 64,
    58, 80, 2, 4, 44,
    30, 6, 50, 37, 82,
    95, 22, 82, 86, 10,
    5, 70, 94, 27, 32,
    13, 63, 79, 1, 57,
    99, 55, 22, 87, 39,
    87, 17, 64, 63
]
# Now new_score will convert the score values to integers.
new_score = int(input("Score? "))
### YOUR CODE STARTS HERE

#here I use append function to add the new_score to the given list of math scores.
scores.append(new_score)

#For  the average I used sum and len function to first add all the scores.
# And then I divided it to length of the list. Then I used print to display the average on screen.
print(sum(scores)/len(scores))

### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
For the CODE I used append function to add the 45th math score to the already existing list of scores. 
After that the work was to find the average. For the average I basically sum up all the values and divided to the 
length of the list using sum and len function.
### YOUR EXPLANATION ENDS HERE
"""