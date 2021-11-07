def selection_sort(alist):
    n = len(alist)
    for i in range(n):
        min_index = i
        for j in range(i + 1 , n):
            if alist[j] < alist[min_index]:
                min_index = j
        
        alist[min_index] , alist[i] = alist[i] , alist[min_index]
