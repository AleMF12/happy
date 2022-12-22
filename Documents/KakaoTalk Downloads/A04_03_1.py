success = False
### YOUR CODE STARTS HERE
correct_pass = '2C08:21'
user_list = []
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

### YOUR EXPLANATION ENDS HERE
"""