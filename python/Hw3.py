import random
import numpy as np


A = np.random.choice([0, 2, 4, 8], (4, 4))
print(A)


def right():


def left():
    for i in range(4):
        if A[i, 2] == 0:
            A[i, 2] = A[i, 3]
            A[i, 3] = 0
        if A[i, 1] == 0:
            A[i, 1] = A[i, 2]
            A[i, 2] = A[i, 3]
            A[i, 3] = 0
        if A[i, 0] == 0:
            A[i, 0] = A[i, 1]
            A[i, 1] = A[i, 2]
            A[i, 2] = A[i, 3]
            A[i, 3] = 0

        if A[i, 0] == A[i, 1]:
            A[i, 0] = A[i, 0]*2
            A[i, 1] = A[i, 2]
            A[i, 2] = A[i, 3]
            A[i, 3] = 0
        if A[i, 1] == A[i, 2]:
            A[i, 1] = A[i, 1]*2
            A[i, 2] = A[i, 3]
            A[i, 3] = 0

        if A[i, 2] == A[i, 3]:
            A[i, 2] = A[i, 2]*2
            A[i, 3] = 0

        print(A)
