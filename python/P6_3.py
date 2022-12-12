def legendre(n, x):
    ### IMPLEMENT YOUR CODE BELOW ###
    if n == 0:
        return 1.
    if n == 1:
        return x

    def P_n2(x):
        P_n2 = 1.
        return P_n2

    def P_n1(x):
        P_n1 = x
        return P_n1

    def P_n(x):
        P_n = ((2*n-1) * x * P_n1(x) -
               (n-1) * P_n2(x))
        return P_n

    if n >= 3:
        for i in range(1, n+1):
            P = (2*n-1) * x * P_n1(x)

    return 0.
