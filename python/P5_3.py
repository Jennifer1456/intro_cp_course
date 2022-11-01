import datetime


def days_since_special_relativity_paper(year, month, day):
    days = 0
    ### START YOUR CODE HERE ###
    age = datetime.date(year, month, day) - datetime.date(1905, 9, 26)
    days = age.days
    #### END YOUR CODE HERE ####
    return days
