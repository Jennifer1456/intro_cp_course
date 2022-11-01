def calculate_sum_of_prime_factors(N):
    sum_of_prime_factors = 0
    ### START YOUR CODE HERE ###

    for i in range(2, N+1):
        # find the factors
        if N % i == 0:
            j = 2
            k = True
            # check if the factor i is prime or not
            while j <= (i)**0.5:
                if i % j == 0:
                    k = False
                j += 1
            if k:
                sum_of_prime_factors += i

    #### END YOUR CODE HERE ####
    return sum_of_prime_factors
