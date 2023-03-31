import math


def evaluate_difference(N):

    ret_value = 0.
    s = 0.
    for i in range(1, N+1):
        s += 1/(i**2)
    ### START YOUR CODE HERE ###
    ret_value = abs(math.pi-(6 * s)**0.5)
    #### END YOUR CODE HERE ####
    return ret_value


def evaluate_difference(N):

    ret_value = 0.
    ret_value = abs(math.pi-math.sqrt(6*sum([1/(i+1)**2 for i in range(N)])))

    #### END YOUR CODE HERE ####
    return ret_value
