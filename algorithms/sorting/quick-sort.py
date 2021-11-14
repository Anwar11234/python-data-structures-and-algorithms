def quick_sort(alist):
    n = len(alist)
    quick_sort_helper(alist , 0 , n - 1)

def quick_sort_helper(alist , first , last):
    if first < last:
        split_point = partition(alist , first , last)

        quick_sort_helper(alist , first , split_point - 1)
        quick_sort_helper(alist , split_point + 1 , last)

def partition(alist , first , last):
    pivot = alist[first]
    left = first + 1
    right = last        

    done = False
    while not done:
        while alist[left] <= pivot and left <= right:
            left += 1

        while alist[right] >= pivot and left <= right:
            right -= 1

        if right < left:
            done = True
        else:
            [alist[left] , alist[right]] =  [alist[right] , alist[left]]      

    [alist[first] , alist[right]] = [alist[right] , alist[first]]

    return right             

