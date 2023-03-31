import scipy.integrate as integrate
from scipy.stats import norm
import math


def nsigma_at_prob(prob):
    nsig = 0.
    ### START YOUR CODE HERE ###
    nsig = norm.ppf((prob + 1)/2)

    #### END YOUR CODE HERE ####
    return float(nsig)
