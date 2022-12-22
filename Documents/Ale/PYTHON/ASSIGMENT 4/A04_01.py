books = [
    "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel",
    "Amos", "Obadiah", "Jonah", "Micah", "Nahum",
    "Habakkuk", "Zephaniah", "Haggai", "Micah", "Zechariah", "Malachi"
]

unique = []
### YOUR CODE STARTS HERE
#First I use for-loop to remove duplicated names of the bible books. So for this I loop through the list and check
#one by one and the if the name of the book is not duplicated it will be store in the list called 'unique'.
#But if it is duplicated the second element will be removed.

for x in books:
    if x not in unique:
        unique.append(x)


### YOUR CODE ENDS HERE
print(unique)

"""
### YOUR EXPLANATION STARTS HERE
Here list of bible books names are provided however there are duplicated names. The task is to remove the duplicated names
and store in the 'unique' list. First I use for-loop to remove duplicated names of the bible books. So for this 
I loop through the list and check one by one and the if the name of the book is not duplicated it will be store in 
the list called 'unique'. But if it is duplicated the second element will be removed.
### YOUR EXPLANATION ENDS HERE
"""