import random
import string


def password_generator():
    password = ''
    ### START YOUR CODE HERE ###
    password = ''.join(random.choice(
        string.ascii_letters + string.digits) for x in range(16))

    #### END YOUR CODE HERE ####
    return password
