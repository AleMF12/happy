#First I assign a value for x
x = " "

# Below I assign a value for "y" that will be the first line of the triangle
# as we need to use concatenation I will just multiply 4 times "x"
y = 4*x

#for the second line I will need 3 spaces so I will multiply 3 times "x"
w = 3*x

#for the second line I will need 2 spaces so I will multiply 2 times "x"
z = 2*x

#for this line I wil just need one space so p is assigned the value of x
p = x

#I assig the asteric symbol to b and use consequtively in concatenation to complete the
#triangule of stars.
b = "*"

# for this line d will be assigned 3 times b
d = 3*b
# for this line f will be assigned 5 times b
f = 5*b
# for this line g will be assigned 7 times b
g = 7*b
# for this line j will be assigned 9 times b
j = 9*b

# Here I call print function to display the string concatenation for the first line
print((y) + (b) + (y))
# Here I call print function to display the string concatenation for the second line
print((w) + (d) + (w))
# Here I call print function to display the string concatenation for the next line
print((z) + (f) + (z))
# Here I call print function to display the string concatenation for the next line
print((p) + (g) + (p))
# Here I call print function to display the string j for the last line
print((j))
