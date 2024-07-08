import typing as tp
from collections import Counter

def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    """
    :param seq: sequence of elements
    :return: number of elements need to drop to leave equal elements
    """
    a=0
    count = Counter(seq)
   
    max_count = max(count.values(),default=0)

    a = len(seq) - max_count
    
    return a


a=[1,2,4,5,6,7,8,8,8,8,8,8]
print(get_min_to_drop(a))



