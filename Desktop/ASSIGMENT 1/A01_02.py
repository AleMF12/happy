#the value is stored in the variable x calling imput function, where the user has to imput a value of x
x = input("x = ")
#the value is stored in the variable y calling imput function, where the user has to imput a value of y
y = input("y = ")

#Below I swapped two number using an additional variable called a
#First I assigned the value of x variable to varaible a. I used int because the user input the value of x and y
# as a string so I had to convert to an integer calling function int.

### YOUR CODE STARTS HERE

a = int(x) ; x = int(y) ; y = int(a)

### YOUR CODE ENDS HERE

#Here the print function will display Swapped message
print("## Swapped")

#The function print will display the swap value of y
print("x =", x)

#The function print will display the swap value of x
print("y =", y)

"""
### YOUR EXPLANATION STARTS HERE
In order to swapped a variable I had to create a third variable called "a" where I assign a value 
integer of x, then I swapped the integer of "y" to "x" and finally assign the integer "a" to "y".
### YOUR EXPLANATION ENDS HERE
"""