prices = [3.16, 5.12, 4.49, 6.12]
data = ["B15", "S10", "B2", "S3"]

total = 100
profit = 0
sum_B = 0
sum_S = 0
### YOUR CODE STARTS HERE
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

B_sum = sum_B
S_sum = sum_S
profit += S_sum - B_sum
total += profit
### YOUR CODE ENDS HERE
print("Balance =", total)
print("Profit =", profit)

"""
### YOUR EXPLANATION STARTS HERE

### YOUR EXPLANATION ENDS HERE
"""