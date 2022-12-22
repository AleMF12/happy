#Here I have defined the variable r as float type, because the input can accept decimals.
# The user is asked to input the value of Radious.
r = float(input("please input the Radious value, r = "))

#we defined the variable pi as it was written in the instructions we assigned that value.
π = 3.141592

#then as it is known the formula to find the area of a circle we just calculated by pi multiplied
# to Radious to the power of 2. And we round it by 3 decimals
A = round(π*r**2, 3)

#I called the print function to print the string Radious plus space plus the value of radious.
#And I used str function for radious to convert it to string because originally it was an integer data type
# I did that so it can concatenate with the other strings.
print("Radious ?" + " " + str(r))

#I print the value of Area string plus space and the value of area.
#And I used "str" function for Area to convert it to string so it can concatenate with the other strings.
print("Area =" + " " + str(A))

#Below I use print function to display space between the expressions
print(" ")

#Below I use print function to displlay the last expression of Assume pi plus the value of pi.
#And I used "str" function for pi to convert it to string so it can concatenate with the other strings.
print("Assume π = " + " " + str(π))
