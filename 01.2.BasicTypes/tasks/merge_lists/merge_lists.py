def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    lst = lst_a+lst_b
    lst.sort()
    return lst


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    lst = lst_a+lst_b
    lst=sorted(lst)
    return lst


ls1=[1,2,4]
ls2=[2,3,4]
print(merge_iterative(ls1,ls2))