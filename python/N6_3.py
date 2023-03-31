import numpy as np

pattern = \
    np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype='int')


def in_central_cell_is_alive(p):
    decision = 0
    S = sum(sum(p))
    if S == 3 or (S == 4 and p[1, 1] == 1):
        decision = 1
    return decision


def game_of_life(n):
    p = pattern.copy()
    P = np.hstack((np.zeros((18, 1)), p, np.zeros((18, 1))))
    P = np.vstack((np.zeros((1, 13)), P, np.zeros((1, 13))))

    for i in range(1, n+1):
        P[0], P[-1], P[:, 0], P[:, -1] = 0, 0, 0, 0
        P2 = P.copy()
        print(P2)
        for j in range(1, P.shape[0]-1):
            for k in range(1, P.shape[1]-1):
                input = np.array([[P[j-1, k-1], P[j-1, k], P[j-1, k+1]],
                                 [P[j, k-1], P[j, k], P[j, k+1]],
                                 [P[j+1, k-1], P[j+1, k], P[j+1, k+1]]])
                if j == 4 and k == 6:
                    print(input)
                    print(in_central_cell_is_alive(input))
                P2[j, k] = in_central_cell_is_alive(input)

        p = P2[1:-1, 1:-1]
        P = P2.copy()
    print(p)
    return p


game_of_life(1)
