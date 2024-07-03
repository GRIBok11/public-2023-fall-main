def find_value(nums: list[int] | range, value: int) -> bool:
    low = 0
    high = len(nums) - 1
    result = False
    while low<=high:
           mid = (low + high) // 2
           guess = nums[mid]
           if guess == value:
            result=True
            return result
           if guess > value:
            high = mid - 1
           else:
            low = mid + 1
    return result  



def filter_list_by_list(lst_a: list[int] | range, lst_b: list[int] | range) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    new_lst_a = lst_a
    black_list=[]
    for val in lst_b:
       if val in black_list:
          continue
       if find_value(lst_a,val) == True:
          new_lst_a = [x for x in new_lst_a if x != val]
          black_list.append(val)
       else :
          pass
    return new_lst_a

a=[1,2,3,4]
b=[1,2,3]

print(filter_list_by_list(a,b))

b=[0] * 10**5

print(b)