import scipy.integrate as integrate
import math
from scipy.stats import norm


def prob_at_nsigma(n):
    prob = 0.
    ### START YOUR CODE HERE ###

    result = integrate.quad(norm.pdf, -n, n)
    prob = result[0]

    #### END YOUR CODE HERE ####
    return prob
