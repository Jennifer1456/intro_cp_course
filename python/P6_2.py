def legendre(n, x):
    ### IMPLEMENT YOUR CODE BELOW ###
    if n == 0:
        return 1.
    if n == 1:
        return x
    if n == 2:
        P = 0.5*(3*x**2-1)
        return P
    if n == 3:
        P = 0.5*(5*x**3-3*x)
        return P

    return 0.
