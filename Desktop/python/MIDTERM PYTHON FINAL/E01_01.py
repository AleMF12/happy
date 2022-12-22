def load_data():
    with open("peter.txt", "rt") as fin:
        data = fin.read()
    
    ### YOUR CODE STARTS HERE
    # First I removed the possible spaces at the beginning and at the end of the line in the file
    # and then I split the verses I was given. To do that I use the function split with the argument
    # '~\n' to split at the end of the line where comes '~'.
    data_splited = data.strip().split("~\n")

    # After that I removed a possible remained '~'
    # Then I replaced the '.~' with "." by creating a new list called "data_list", without "~" with each verse
    # as one element in the list.
    data_list = [i.replace('.~', '.') for i in data_splited]

    # Here I return the list as an output.
    return data_list
    ### YOUR CODE ENDS HERE

lines = load_data()






