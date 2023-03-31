import numpy as np
import scipy.linalg as linalg


def give_me_a_matrix(A, B, C):
    output = np.zeros((2, 2))
    ### START YOUR CODE HERE ###
    output[0, 0] = np.linalg.det((A + B.dot(np.linalg.inv(C))))
    output[0, 1] = np.linalg.det((B - C.dot(np.linalg.inv(A))))
    output[1, 0] = np.linalg.det((B - A.dot(np.linalg.inv(C))))
    output[1, 1] = np.linalg.det((A + C.dot(np.linalg.inv(B))))

    #### END YOUR CODE HERE ####
    return output


A = np.array([[0.8415496,  0.69344269],
              [0.85639808, 0.21239206]])
B = np.array([[0.8415496,  0.69344269],
              [0.85639808, 0.21239206]])
C = np.array([[0.8415496,  0.69344269],
              [0.85639808, 0.21239206]])
print(give_me_a_matrix(A, B, C))
