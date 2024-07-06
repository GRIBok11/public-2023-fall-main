from collections.abc import Sequence


def find_median(nums1: Sequence[int], nums2: Sequence[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """

    listt=[]
    listt = nums1 + nums2
    listt.sort()
 
    n=listt.__len__()
   
    if n==1:
        return float(listt[0])
    elif n % 2==1:
        b=listt[(n//2)]
    
        return float(b)
    else:
        n-=1
        a= (listt[(n//2)]+ listt[(n//2)+1])/2
        a:float
        return float(a)
        
a=[]
b=[1,2,3]
print(find_median(a,b))
print(find_median([1, 2], [3, 4]))

