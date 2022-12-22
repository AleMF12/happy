prices = [3.16, 5.12, 4.49, 6.12]
data = ["B15", "S10", "B2", "S3"]

total = 100
profit = 0
sum_B = 0
sum_S = 0
### YOUR CODE STARTS HERE
#In this part the task was to compute the final balance and the profit that is earned.
#So for this I used for -loop to loop through the data list and then I used if statement to extract the first element of the string.
#in each element of data list.
#And I asssigned to the variable sold_1 in index of both stocks. After doing this I created another variable num_1
#I assigned to it the value of each stock sold followed by extract from price, respective price of the sold stock
#Then we multiply the number of stocks times the price of the stock. Then I sum up all the sold stocks.
#The same process goes to 'sold- stock' which is in the 'else' statement.
for stock in data:
    if stock[0] == 'B':
        sold_1= int(data.index(stock))
        num_1 = int(stock[1:])
        price_1 = prices[sold_1]
        B_stock = price_1*num_1
        sum_B += B_stock


    else:
        sold_2 = (data.index(stock))
        num_2 = int(stock[1:])
        price_2 = prices[sold_2]
        S_stock = price_2*num_2
        sum_S += S_stock
#First we assign the profit value equal to the sold-sum minus the old-sum.
#The the total equal to first balance plus profit.
B_sum = sum_B
S_sum = sum_S
profit += S_sum - B_sum
total += profit
### YOUR CODE ENDS HERE
print("Balance =", total)
print("Profit =", profit)

"""
### YOUR EXPLANATION STARTS HERE
Here the task was to compute the final balance and the profit that is earned.
#So for this I used for -loop to loop through the data list and then I used 
if statement to extract the first element of the string in each element of data list.
And I assigned to the variable sold_1 in index of both stocks. After doing this I created another variable num_1
I assigned to it the value of each stock sold followed by extract from price, respective price of the sold stock
Then we multiply the number of stocks times the price of the stock. Then I sum up all the sold stocks.
The same process goes to 'sold- stock' which is in the 'else' statement.
Finally the value of balance and profit will be display on the screen.
### YOUR EXPLANATION ENDS HERE
"""