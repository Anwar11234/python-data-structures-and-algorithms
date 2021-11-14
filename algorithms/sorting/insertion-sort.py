def insertion_sort(alist):
    n = len(alist)
    for i in range(1 , n):
        value = alist[i]
        pos = i
        while pos > 0 and value < alist[pos - 1]:
            alist[pos] = alist[pos - 1]
            pos -= 1

        alist[pos] = value    
