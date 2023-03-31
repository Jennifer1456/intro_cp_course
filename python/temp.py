import numpy as np


def in_central_cell_is_alive(p):
    decision = 0
    S = sum(sum(p))
    if S == 3 or (S == 4 and p[1, 1] == 1):
        decision = 1
    return decision


P = np.random.choice([0, 2, 4, 8], (7, 10))
print(P)
for j in range(1, P.shape[0]-1):
    for k in range(1, P.shape[1]-1):
        input = np.array([[P[j-1, k-1], P[j-1, k], P[j-1, k+1]],
                          [P[j, k-1], P[j, k], P[j, k+1]],
                          [P[j+1, k-1], P[j+1, k], P[j+1, k+1]]])
        if j == 4 and k == 6:
            print(input)
            print(in_central_cell_is_alive(input))
