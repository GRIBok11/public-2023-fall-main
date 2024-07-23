def get_squares(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with squared values
    """
    return [x ** 2 for x in elements]



# ====================================================================================================


def get_indices_from_one(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with indices started from 1
    """
    i=1
    l= len(elements)
    index=[]
    while i!=l+1:
        index.append(i)
        i+=1
    
    list(range(1, l + 1))
    return list(range(1, len(elements) + 1))



# ====================================================================================================
def get_max_element_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of maximum element if exists, None otherwise
    """
    if not elements:
        return None
    max_index = 0
    i = 0
    max = elements[0]
    while i < elements.__len__():
        if elements[i] > max:
            max = elements[i]
            max_index = i
        i += 1
    return max_index



# ====================================================================================================


def get_every_second_element(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with each second element of list
    """
    i=0
    l=[]
    while i<elements.__len__():
        if i%2==1:
            l.append(elements[i])
        i+=1
    
    elements[1::2]
    return elements[1:len(elements)+1:2]





# ====================================================================================================


def get_first_three_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of first "3" in the list if exists, None otherwise
    """
    i=0
    while i<elements.__len__():
        if elements[i]==3:
           return i
        i+=1

    return None


# ====================================================================================================


def get_last_three_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of last "3" in the list if exists, None otherwise
    """
    n = elements.__len__()-1
    while n >= 0:
        if elements[n] == 3:
            return n
        n -= 1
    
    return None


# ====================================================================================================


def get_sum(elements: list[int]) -> int:
    """
    :param elements: list with integer values
    :return: sum of elements
    """
    return sum(elements)


# ====================================================================================================


def get_min_max(elements: list[int], default: int | None) -> tuple[int | None, int | None]:
    """
    :param elements: list with integer values
    :param default: default value to return if elements are empty
    :return: (min, max) of list elements or (default, default) if elements are empty
    """

    return min(elements,default=default), max(elements,default=default)


# ====================================================================================================


def get_by_index(elements: list[int], i: int, boundary: int) -> int | None:
    """
    :param elements: list with integer values
    :param i: index of elements to check with boundary
    :param boundary: boundary for check element value
    :return: element at index `i` from `elements` if element greater then boundary and None otherwise
    """
    return elements[i] if elements[i] > boundary else None


val=[1,2,3,4,5,3]

print(get_squares(val))

print(get_indices_from_one(val))
print(get_max_element_index(val))
print(get_every_second_element(val))
print(get_first_three_index(val))
print(get_last_three_index(val))
print(get_sum(val))
print(get_min_max(val,0))
print(get_by_index(val,3,2))