def find_greatest_common_factor(M, N):
    greatest_common_factor = 0
    ### START YOUR CODE HERE ###
    i = 1
    for i in range(1, max(M, N)+1):
        if M % i == 0 and N % i == 0:
            if greatest_common_factor <= i:
                greatest_common_factor = i
        i += 1

    #### END YOUR CODE HERE ####
    return greatest_common_factor
