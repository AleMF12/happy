from E01_01 import load_data
lines = load_data()
### YOUR CODE STARTS HERE
#First I define a list called bible.
bible = []
#Here I used for loop to iterate through each element of the list line.
#In order to create the tuple with four elements, I took each element of the line list and I split it
# with "|" so that I get 4 elements split.
#After that I built a tuple with 4 elements which are name of the book, chapter number, verse number and text.
# I extracted the bible names by using the code ver[0] then by using the function int to convert the extracted
# chapter number with the code ver[1],the same goes to verse number and text.
#Finally I append the built tuple to the list.

for bible_verse in lines:
    ver = bible_verse.split("|")
    book = (ver[0],int(ver[1]),int(ver[2]),ver[3])
    bible.append(book)


#now I assigned the value name of the book to the variable 'vers'
vers = 'Pe2'

#In this part I loop through the bible list elements, and then after looping that I verify in each element if contain
#verse second Peter, chapter 1, verse 10, after that I printed on screen the text corresponded to the chapter and verse.
for i in bible:
    if vers in i:
        if i[1] == 1 and i[2] == 10:
            print(i[3].strip())
### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
Basically in this program I created a new list variable called bible, and used a for loop and iterate through each
 verse in the lines variable. A tuple contains four elements which are the name of the book, the chapter and 
 verse number and text. Finally this tuple is appended to the bible list and use then extracted Peter chapter 1 verse 10.
Here I removed the empty space in the text.
### YOUR EXPLANATION ENDS HERE
"""