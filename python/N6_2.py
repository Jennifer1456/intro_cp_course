import numpy as np


def central_cell_is_alive(p):
    decision = True
    ### START YOUR CODE HERE ###
    if p[1, 1] == 1:
        p[1, 1] = 0
        S = sum(sum(p))
        if S < 2 or S > 3:
            decision = False
        elif S == 2 or S == 3:
            decision = True

    if p[1, 1] == 0:
        decision = False
        S = sum(sum(p))

        if S == 3:
            decision = True

    #### END YOUR CODE HERE ####
    return decision


def central_cell_is_alive(p):
    decision = False
    S = sum(sum(p))

    if S == 3 or (S == 4 and p[1, 1] == 1):
        decision = True
    #### END YOUR CODE HERE ####
    return decision


p = np.array([[0,  0,  0],
              [0,  0,  1],
              [0,  0,  1]], dtype='int')
print(central_cell_is_alive(p))
