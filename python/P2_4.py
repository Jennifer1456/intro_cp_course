sum_of_series = 0.
### START YOUR CODE HERE ###

for n in range(1, 101):
    if n % 2 == 0:
        sum_of_series += -1/n
    else:
        sum_of_series += 1/n

#### END YOUR CODE HERE ####
print('value:', sum_of_series)
