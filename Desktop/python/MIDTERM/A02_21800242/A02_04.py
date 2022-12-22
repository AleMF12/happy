# Here animals is the name assigned to the list of strings
animals = ["dog", "cat", "alligator", "cow", "Snake", "elephant", "Chicken"]

### YOUR CODE STARTS HERE
#Here I use the sort function to sort out the list of animal where alligator string will be
#the first and snake the last.
animals.sort(reverse=True, key = lambda word: word[-3:-1])

### YOUR CODE ENDS HERE
# the print function will display the re-organized list.
print(animals)

"""
### YOUR EXPLANATION STARTS HERE
The function sort is used to organize the list of animals.
The function has 2 parameters. One of them is called reverse and another key.
Where reverse by default is false, which means the least is in increasing sequence
while reverse equal to true which means the opposite.
Key parameter is where the user should define the function, which user will use  
to sort the list as the user desires. Where lamda is a unknown function which 
I defined to organize the list. Which I defined the variable word and then
I sliced from the variable or list. From the end -1 to -3 indexes.

References
https://www.w3schools.com/python/ref_list_sort.asp
https://realpython.com/python-sort/
### YOUR EXPLANATION ENDS HERE
"""