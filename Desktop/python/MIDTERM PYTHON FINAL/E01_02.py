from E01_01 import load_data
lines = load_data()
### YOUR CODE STARTS HERE
# First I created a variable and then assign book name, chapter and verse.
#Second I created another variables wich are book1, book2, ver_or_1, ver_or_2.
#And then I assigned a value to these variables.
user = '1 Peter 4:7'
book1 = 'Pe1'
book2 = 'Pe2'
ver_or_1 = '1 Peter'
ver_or_2 = '2 Peter'

#In this code line, I iterated trough the verse list and, then I split each element with space.
# to get each element as new element.
word = [verse.split(" ") for verse in lines]

#In this stage I used for loop to iterate trough all the elements in the word list . And the I aplit
#it on every first element of the word list in order to get book name, chapter and verse.
#I extracted the first element of the split list in order to get the book name and then replace every name
#of the list to the name that I created.
#Then I extracted from the split list called "bo_chap_ver" the book, chapter and the verse consecutively.
#After that I create a variable called  'cha_ver', where we assigned the variable cha and 'ver' separeted by colon
#then I created a variable "book_cha_ver" to put togheter the book, chapter and verse.
# Finally, I use if statement and replace in the list the book, chapter and verse number with empty space. After adding
#the empty space I removed the same empty espace by applying the function strip.
for i in word:
    bo_chap_ver = i[0].split("|")
    book_name = bo_chap_ver[0].replace(book1, ver_or_1).replace(book2, ver_or_2)
    cha = bo_chap_ver[1]
    ver = bo_chap_ver[2]
    cha_ver = f"{cha}:{ver}"
    book_cha_ver = f"{book_name} {cha_ver}".strip()
    if user == book_cha_ver:
        i[0] = ''
        text = " ".join(i).strip()
        print(text)

### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
I created a program which main function is to look into the list of bible books to find specific bible verse.
the detailed explanation is explained in every line of the program. 
### YOUR EXPLANATION ENDS HERE
"""