def linear_search(list , target):
    for i in range(len(list)):
        if list[i] == target:
            return True

    return False        

# linear search on a sorted sequence

def sorted_linear_search(list , target):
    for i in range(len(list)):
        if list[i] == target:
            return True
        elif list[i] > target:
            return False

    return False            