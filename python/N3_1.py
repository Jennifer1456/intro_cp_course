import math
import numpy


def func(n, x):
    value = 0.
    ### START YOUR CODE HERE ###
    value = sum([x**i for i in range(n+1)])
    #### END YOUR CODE HERE ####
    return value


def func_integrated_numerical(n):
    value = 0.
    ### START YOUR CODE HERE ###
    h = 1.0E-3

    value = sum([(func(n, i)+func(n, i+h))*h /
                2 for i in numpy.arange(-1, 1, h)])

    #### END YOUR CODE HERE ####
    return float(value)


def func_integrated_analytical(n):
    value = 0.
    ### START YOUR CODE HERE ###
    for i in range(n+1):
        value += (pow(1, i+1) - pow(-1, i+1))/(i+1)
    #### END YOUR CODE HERE ####
    return value
