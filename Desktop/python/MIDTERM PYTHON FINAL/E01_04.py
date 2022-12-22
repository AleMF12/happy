from E01_01 import load_data
lines = load_data()
### YOUR CODE STARTS HERE
#In this part I have named the dicctionary as bible
bible = {}
#Then I iterated trough the line list to get each verse and then I split each element using "|"
#After that I extracted the name of the book, the verse, and chapter number and verse number.
# After I created a tuple using those 3 elements. And finally I used the tuple as the key of the dictionary
#and  text as a value.
for bible_verse in lines:
    ver = bible_verse.split("|")
    key = (ver[0],int(ver[1]),int(ver[2]))
    bible[key] = ver[3].strip()
#Here I created a tuple assigned to variable called value. So that I can structed the first Peter chapter 4 verse 13.
value = ('Pe1', 4, 13)

# Finally I use print function to display on the screen the result of the value variable extracted from the dictioray bible.
print(bible[value])
### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
In this part the work was basically to create a new dictionary variable that I called bible . Initially, this dictionary will be empty.
I used a for loop and iterate through each verse in the lines variable of the text file. I constructed a tuple with the
next three elements, the book, chapter verse number. Then I removed empty space in the bible text.
### YOUR EXPLANATION ENDS HERE
"""