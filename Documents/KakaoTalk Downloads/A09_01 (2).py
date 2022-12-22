### YOUR CODE STARTS HERE
bible_fullname = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel',
                  '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job',
                  'Psalm','Proverbs','Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel',
                  'Daniel', 'Hosea', 'Joel','Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk','Zephaniah',
                  'Haggai','Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians',
                  '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians',
                  '2 Thessalonians','1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter',
                  '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation']

with open("bible-3letter.txt", "rt") as fin:
    data_abbre = fin.read()

with open("Bible-fullname.txt", "rt") as fin:
    data_full = fin.read()

book_full = data_full.strip().split("\n")

book_abbre = data_abbre.strip().split("\n")

book_abbre.remove("Ahh")

full2abbrev = {}

new_book = []
for bible in bible_fullname:
    if bible in book_full:
        new_book.append(bible)
    elif bible not in book_full:
        new_book.append(bible)

with open("bible-fullname.txt", "w") as f:
    for line in new_book:
        if line.strip("\n") != "nickname_to_delete":
            f.write(f"{line}\n")

for i in range(66):
    if book_full[i].split(" ")[0] == '1':
        if book_full[i].split(" ")[1:4][0][:2]+book_full[i].split(" ")[0] == book_abbre[i]:
            full2abbrev[book_full[i]] = book_abbre[i]
    elif book_full[i].split(" ")[0] == '2':
        if book_full[i].split(" ")[1:4][0][:2]+book_full[i].split(" ")[0] == book_abbre[i]:
            full2abbrev[book_full[i]] = book_abbre[i]
    elif book_full[i].split(" ")[0] == '3':
        if book_full[i].split(" ")[1:4][0][:2]+book_full[i].split(" ")[0] == book_abbre[i]:
            full2abbrev[book_full[i]] = book_abbre[i]
    else:
        if book_full[i].split(" ")[0][:3] == book_abbre[i]:
            full2abbrev[book_full[i]] = book_abbre[i]

abbrev2full = {}

for j in range(66):
    if book_abbre[j][-1] == '1':
        if book_abbre[j] == book_full[j].split(" ")[1:4][0][:2]+book_full[j].split(" ")[0]:
            abbrev2full[book_abbre[j]] = book_full[j]

    elif book_abbre[j][-1] == '2':
        if book_abbre[j] == book_full[j].split(" ")[1:4][0][:2]+book_full[j].split(" ")[0]:
            abbrev2full[book_abbre[j]] = book_full[j]

    elif book_abbre[j][-1] == '3':
        if book_abbre[j] == book_full[j].split(" ")[1:4][0][:2]+book_full[j].split(" ")[0]:
            abbrev2full[book_abbre[j]] = book_full[j]

    else:
        if book_abbre[j] == book_full[j].split(" ")[0][:3]:
            abbrev2full[book_abbre[j]] = book_full[j]

### YOUR CODE ENDS HERE

print(full2abbrev["Genesis"])
print(full2abbrev["Matthew"])
print(full2abbrev["1 Peter"])
print(full2abbrev["Isaiah"])

print(abbrev2full["Exo"])
print(abbrev2full["Rom"])

"""
### YOUR EXPLANATION STARTS HERE

I created a dictionary called full2abbrev that translates the name of the Bible book to the
corresponding 3-letter abbreviation. Also abbrev2full was created  in order to translate
the 3-letter abbreviation back to the corresponding full book name.

### YOUR EXPLANATION ENDS HERE
"""