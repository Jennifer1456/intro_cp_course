import numpy as np


def cov_to_corr(covariance):
    correlation = covariance.copy()
    ### START YOUR CODE HERE ###

    for i in range(correlation.shape[0]):
        for j in range(correlation.shape[1]):
            # print(correlation[i, j])
            correlation[i, j] = covariance[i, j] / \
                covariance[i, i] ** 0.5 / covariance[j, j] ** 0.5
            # print(correlation[i, j])

    #### END YOUR CODE HERE ####
    return correlation


C = np.array([[2., 4.], [3., 1.]])
print(cov_to_corr(C))
print(C[0, 1]/C[0, 0]**0.5/C[1, 1]**0.5)
