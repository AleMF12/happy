def read_test_data(filename):
    data = []
    with open(filename, "rt") as fin:
        lines = fin.read().strip().split("\n")
        for line in lines:
            row = line.split(" ")
            data.append(row)
    return data
    
def display_board(data):
    for row in data:
        print(" ".join(row))

tic_tac_toe = read_test_data(filename="test-data.txt")
print("== 3x3 Matrix (a list in a list) ==")
print(tic_tac_toe)
print()
print("== Tic-Tac-Toe Board ==")
display_board(tic_tac_toe)

### YOUR CODE STARTS HERE

### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE

### YOUR EXPLANATION ENDS HERE
"""