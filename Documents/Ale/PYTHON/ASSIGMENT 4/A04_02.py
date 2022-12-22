matrix_A = [
    [1,2],
    [3,4]
]

matrix_B = [
    [5,6],
    [7,8]
]

matrix_C = [
    [None,None],
    [None,None]
]

### YOUR CODE STARTS HERE
#Here I am using a nested for- loop to perform matrix addition. The idea here is that the first loop will be extracting
#each element of the row. Then the other loop is extracting each element of the matrix in the column. In the rows and the columns
# there is addition.
for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
        matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j]


### YOUR CODE ENDS HERE
#Finally I used print function to print the result of the addition of the matrixs
print(matrix_C)

"""
### YOUR EXPLANATION STARTS HERE
The program is to perform a matrix addition for that I used a nested for-loop to perform it. 
The idea here is that the first loop will be extracting each element of the row. 
Then the other loop is extracting each element  of the matrix in the column. In the rows and the columns
there is addition of the elements.
Finally I used print function to print the result of the addition of the matrices.
### YOUR EXPLANATION ENDS HERE
"""