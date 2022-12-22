records = [["John", 90, 80, 79], ["Daniel", 84, 99, 91], ["Isaiah", 95, 80, 72]]
transcripts = {}
### YOUR CODE STARTS HERE
#I used for loop to look thorough the 'records' list. And extract the score of each student and assign them
#the variable called scores. And then I extracted each student name and assign to the variable called name
#and then I calculated the average of each students scores. And then I assigned the key to the dictionary as name
#and value 'avg'
for student in records:
    scores = [student[1],student[2],student[3]]
    name = student[0]
    avg = sum(scores)/len(scores)
    transcripts[name] = avg
### YOUR CODE ENDS HERE
for name, avg in transcripts.items():
    print(f"{name}'s average = {avg:.2f}")
    
"""
### YOUR EXPLANATION STARTS HERE
Here the task was basically to calculate  students average exam score.
I used for loop to look through the 'records' list. And extract the score of each student and assign them
the variable called scores. And then I extracted each student name and assign to the variable called name
and then I calculated the average of each students scores. After that  I assigned the key to the dictionary as name
and value 'avg'.
Finally the average of the students will be printed.
### YOUR EXPLANATION ENDS HERE
"""    