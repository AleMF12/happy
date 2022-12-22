records = [["John", 90, 80, 79], ["Daniel", 84, 99, 91], ["Isaiah", 95, 80, 72]]
transcripts = {}
### YOUR CODE STARTS HERE
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

### YOUR EXPLANATION ENDS HERE
"""    