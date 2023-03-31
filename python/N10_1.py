import numpy as np


def give_me_a_matrix(A, B, C):
    output = np.zeros_like(A)
    ### START YOUR CODE HERE ###

    output = A.dot(A) + B.dot(B) + C.dot(C) - A.dot(B) - \
        B.dot(C) - C.dot(A)+4*np.eye(A.shape[0])

    #### END YOUR CODE HERE ####
    return output


A = np.array([[0.8415496,  0.69344269],
              [0.85639808, 0.21239206]])
B = np.array([[0.8415496,  0.69344269],
              [0.85639808, 0.21239206]])
C = np.array([[0.8415496,  0.69344269],
              [0.85639808, 0.21239206]])
print(give_me_a_matrix(A, B, C))
