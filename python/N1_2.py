import math


def evaluate_difference(N):
    ret_value = 0.
    ### START YOUR CODE HERE ###
    ret_value = abs(math.e-sum([1/math.factorial(i) for i in range(N)]))

    #### END YOUR CODE HERE ####
    return ret_value
