#Here the variable is defined as search.
# The user is asked to input the value of search.

search = input("?")

### YOUR CODE STARTS HERE
#Here I use the function split to divide the variable in ':' into two parts
x= search.split(":")

#Now I assigned 'y' to the first string with index equal to 0
y= x[0]

#Here the variable y will be split again. Where I call it 'z'
z= y.split(" ")

#now I use the function join to put togheter the string with
# index from 0 to the length of z minus 1.
#Here the key is to find a general formula for the book value.
#So the computer can read the code with book inputs
# like psalm or 2 corinthians

book = " ".join(z)[0:len(z)-1]

#Here for chapter I am calling the last value.
chapter = z[-1]

#for verse the value with index number 1 is called.
verse = x[1]

### YOUR CODE ENDS HERE
# Here the function print used to display the book, chapter and verse
#when it prints, it will show the string and the variable.
print("Book =", book)
print("Chapter =", chapter)
print("Verse =", verse)

"""
### YOUR EXPLANATION STARTS HERE
In this code we are asked to store a Bible verse string and then display book, chapter and verse. 
For this we use the function split to divide the value 2 times. Next to display the value of the book
was necessary to create a general formula that can display s value like psalm and 2 corinthians.  
### YOUR EXPLANATION ENDS HERE
"""