import numpy as np


def prod(x):
    ret_value = 1
    for i in range(4):
        ret_value *= np.cos((i+1)*np.pi*x/2)*np.cosh(x) + \
            np.sin((i+1)*np.pi*x/2)*np.sinh(x)
    return ret_value


def give_me_an_array(x):
    output = np.ones_like(x)
    ### START YOUR CODE HERE ###
    output = prod(x)

    #### END YOUR CODE HERE ####
    return output
