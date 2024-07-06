def reverse_iterative(lst: list[int]) -> list[int]:
    """
    Return reversed list. You can use only iteration
    :param lst: input list
    :return: reversed list
    """
    reverse_list=[]
    i=lst.__len__()
    while i>0:
        reverse_list.append(lst[i-1])
        i-=1
    return reverse_list


def reverse_inplace_iterative(lst: list[int]) -> None:
    """
    Revert list inplace. You can use only iteration
    :param lst: input list
    :return: None
    """
    i=0
    n=lst.__len__()-1
    val=0
    while  i<n:
        val=lst[n]
        lst[n]=lst[i]
        lst[i]=val
        i+=1
        n-=1

    return lst


def reverse_inplace(lst: list[int]) -> None:
    """
    Revert list inplace with reverse method
    :param lst: input list
    :return: None
    """
    lst.reverse()
    return lst


def reverse_reversed(lst: list[int]) -> list[int]:
    """
    Revert list with `reversed`
    :param lst: input list
    :return: reversed list
    """
  
    a=list(reversed(lst))
    return a


def reverse_slice(lst: list[int]) -> list[int]:
    """
    Revert list with slicing
    :param lst: input list
    :return: reversed list
    """
    new_lst=[]
    for val in lst[::-1]:
        new_lst.append(val)
    return new_lst

mas=[1,2,3,4,6,7]

nech_mas=[1,2,3]

mas1=[1,2,3,4,5,6,7]

print(reverse_iterative(mas))
print(reverse_inplace_iterative(nech_mas))
print(reverse_inplace(mas))
print(reverse_reversed(mas1))
print(reverse_slice(mas1))