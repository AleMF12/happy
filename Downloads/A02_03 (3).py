search = input("?")

### YOUR CODE STARTS HERE
x = search.split(":")
y = x[0]
z= y.split(" ")
book = " ".join(z[0:len(z)-1])
chapter = z[-1]
verse = x[1]
### YOUR CODE ENDS HEREx
print("Book =", book)
print("Chapter =", chapter)
print("Verse =", verse)
"""
### YOUR EXPLANATION STARTS HERE

### YOUR EXPLANATION ENDS HERE
"""