

def pronounce_the_number(N):
    number_in_text = 'zero'
    ### START YOUR CODE HERE ###
    aa = ['One', 'Two', 'Three', 'Four', 'Five',
          'Six', 'Seven', 'Eight', 'Nine', 'Ten',
          'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
          'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
    if N >= 1:
        number_in_text = aa[N-1]
    #### END YOUR CODE HERE ####
    return number_in_text


print(pronounce_the_number(0))
