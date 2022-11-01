def find_least_common_multiple(M, N):
    greatest_common_factor = 0
    least_common_multiple = 1
    ### START YOUR CODE HERE ###
    i = 1
    for i in range(1, max(M, N)+1):
        if M % i == 0 and N % i == 0:
            if greatest_common_factor <= i:
                greatest_common_factor = i
        i += 1
    least_common_multiple = M * N/greatest_common_factor
    #### END YOUR CODE HERE ####
    return int(least_common_multiple)
