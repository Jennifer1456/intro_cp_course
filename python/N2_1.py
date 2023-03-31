import math


def func(x):
    value = 1.
    ### START YOUR CODE HERE ###
    for i in range(4):
        value *= math.cos((i+1)*math.pi*x/2)*math.cosh(x) + \
            math.sin((i+1)*math.pi*x/2)*math.sinh(x)

    #### END YOUR CODE HERE ####
    return value


def func_first_derivative(x):
    value = 1.
    ### START YOUR CODE HERE ###
    h = 1.0E-3
    value = (8.*func(x+h/4.)+func(x-h/2.)-8.*func(x-h/4.)-func(x+h/2.))/(h*3.)

    #### END YOUR CODE HERE ####
    return value
