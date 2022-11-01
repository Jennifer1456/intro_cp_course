def calculate_sum_of_factors(N):
    sum_of_factors = 0
    ### START YOUR CODE HERE ###
    for i in range(1, N+1):
        if N % i == 0:
            sum_of_factors += i

    #### END YOUR CODE HERE ####
    return sum_of_factors
