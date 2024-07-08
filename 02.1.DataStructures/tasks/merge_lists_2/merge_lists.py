import typing as tp
import heapq
def iterative_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

 
    
def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    heap = []
    a=[]
    for i, lst in enumerate(seq):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    #return heap
    for val in seq:
        a=a+val
    iterative_sort(a)
    return a

    

   
 
a=[[12,13,14],[1,2,3,4,5],[10,7,8,9]]
print(merge(a))

