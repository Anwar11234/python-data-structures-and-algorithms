def binary_search(list , target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return True
        elif list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False

# recursive binary search

def recursive_binary_search(list , target):
    if len(list) == 0:
        return False
    mid = len(list) // 2
    if list[mid] == target:
        return True
    elif list[mid] > target:
        return recursive_binary_search( list[:mid] , target)
    else:
        return recursive_binary_search(list[mid+1:] , target)        

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))        