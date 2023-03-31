"""def test_perm(my_list):
    
    L = len(my_list)
    ans_list = [my_list] * L * (L-1)
    ans_list[0] = my_list

    temp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = temp

    ans_list[1] = my_list
    
    new_list = []
    for aa in my_list:
        new_list[0] = aa
        my_list.remove(aa)
        
    while my_list:
        item = my_list.pop()
        print(f"Processing item: {item}")

    return ans_list, temp

    # print(perm([1, 2, 3]))
    # for element in my_list:
    #   print(element)
    #  my_list.append(5)
my_list = [1, 2, 3, 6, 5]

for aa in my_list:
    print(aa)


def take_first_number_out(list_to_be_removed):
    new_list = []
    for aa in list_to_be_removed:
        new_list[0] = aa
        list_to_be_removed.remove(aa)
        
        return new_list, list_to_be_removed
"""


def take_first_number_out(input):
    all_list = [[], []]
    i = 0
    list_to_be_removed = input
    new_list = []
    for aa in input:
        new_list = []
        list_to_be_removed = input.copy()
        new_list.append(aa)
        list_to_be_removed.remove(aa)

        all_list[0].append(new_list)
        all_list[1].append(list_to_be_removed)
    return all_list


def perm(list):
    all_list = take_first_number_out(list)
    first = all_list[0].copy()
    remain = all_list[1].copy()
    aa = take_first_number_out(remain[0])

    print(first, remain, aa)


perm([3, 5, 6])
