import scipy.integrate as integrate
import math


def convoluted_BreitWigner(E, M, Gamma, sigma):
    value = 0.
    ### START YOUR CODE HERE ###
    result = integrate.quad(lambda x: math.exp(-(x**2)/(2*sigma**2)) /
                            (((E-x)**2-M**2)**2+M**2*Gamma**2), -3*sigma, 3*sigma)
    value = result[0]

    #### END YOUR CODE HERE ####
    return value

# lambda x: 以x為變數的匿名function。lambda: 系統指令。就跟def import...之類的一樣，是保留字。
