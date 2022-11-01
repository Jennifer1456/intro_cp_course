import math
func = 0.
### START YOUR CODE HERE ###


def sigma_1(first, last, const):
    sum = 0
    for i in range(first, last + 1):
        sum += const ** i
    return sum


def sigma_2(first, last, const):
    sum = 0
    for i in range(first, last + 1):
        sum += const * i
    return sum


func = math.log(sigma_2(1, 3, sigma_1(1, 3, math.pi)))

#### END YOUR CODE HERE ####
print('value:', func)
