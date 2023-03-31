import numpy as np


def g_give_me_an_array(A, B):
    output = np.array([])
    ### START YOUR CODE HERE ###
    output = np.empty([5*A.shape[0], 5*A.shape[1]])
    for i in range(A.shape[0]):
        output[i] = np.array([A[i], B[i], A[i], B[i], A[i]]).reshape(-1)
    for i in range(A.shape[0]):
        j = i + A.shape[0]
        output[j] = np.array([B[i], A[i], B[i], A[i], B[i]]).reshape(-1)
    for i in range(A.shape[0]):
        j = i + 2*A.shape[0]
        output[j] = np.array([A[i], B[i], A[i], B[i], A[i]]).reshape(-1)
    for i in range(A.shape[0]):
        j = i + 3*A.shape[0]
        output[j] = np.array([B[i], A[i], B[i], A[i], B[i]]).reshape(-1)
    for i in range(A.shape[0]):
        j = i + 4*A.shape[0]
        output[j] = np.array([A[i], B[i], A[i], B[i], A[i]]).reshape(-1)

    # output = np.append([A], [B])
    # output = output.reshape(-1)
    # output = output.reshape((2*A.shape[0]), (2*A.shape[1]))
    # print(output)
    #### END YOUR CODE HERE ####
    return output


def give_me_an_array(A, B):
    H1 = np.hstack((A, B, A, B, A))
    H2 = np.hstack((B, A, B, A, B))
    output = np.vstack((H1, H2, H1, H2, H1))
    return output


A = np.array([[0, 5, 1, 7, 7]])
B = np.array([[0, 3, 7, 3, 5]])

A = np.array([[9],
              [2]])
B = np.array([[6],
              [3]])


A = np.array([[9, 6, 3],
              [2, 8, 7]])
B = A+1
print(give_me_an_array(A, B))
