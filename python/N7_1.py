import numpy as np
import matplotlib.pyplot as plt


def give_me_a_line(c):
    output = plt.plot([], [])
    ### START YOUR CODE HERE ###
    x = np.linspace(0, 1, 101)
    y = np.zeros(101)
    for i, e in enumerate(c):
        y += e*x**i
    output = plt.plot(x, y)
    #### END YOUR CODE HERE ####
    return output[0]
