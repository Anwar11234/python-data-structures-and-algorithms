def bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1 , 0 , -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j] , alist[j + 1] = alist[j + 1] , alist[j]    

def smart_bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1 , 0 , -1):
        exchanges = False
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j] , alist[j + 1] = alist[j + 1] , alist[j]
                exchanges = True     

        if not exchanges:
            break            