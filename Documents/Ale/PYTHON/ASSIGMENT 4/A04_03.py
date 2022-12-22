success = False
### YOUR CODE STARTS HERE
#Here the application of the program is to interact with the user so he can have granted access
#only he writes the correct password. Otherwisw he will be denied access after three attempts.


#I assigned correct password variable to the value password.
correct_pass = '2C08:21'
#I created an empty list and assigned used-list name
user_list = []
#Here I use while loop and as a condition to loop I used the key word 'not'to allow to loop
#thorugh the user list which is the list where the elements from the user input are.
#Then I assigned the user input function.
#Additionally I append to the user list the attemps of the user.

while not success:
    user = input("Insert the password: ")
    user_list.append(user)
    if user == correct_pass:
        success = True
    elif len(user_list) == 3:
        success = False
        break
### YOUR CODE ENDS HERE
if success:
    print("Access granted!")
else:
    print("Your account is locked.")

"""
### YOUR EXPLANATION STARTS HERE
Here in this part we have to access granted only, in this program we should allow
the user the user to enter the password in 3 attempts.
To so this I use while loop and as a condition to loop I used the key word 'not' to allow to loop
through the user list which is the list where the elements from the user input are.
Then I assigned the user input function. Additionally I append to the user list the attempts of the user.
Finally I I use print function to print, "Access granted!" when is correct or "Your account is locked." when is incorrect.
### YOUR EXPLANATION ENDS HERE
"""