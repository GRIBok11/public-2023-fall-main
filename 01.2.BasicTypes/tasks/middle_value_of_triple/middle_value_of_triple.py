def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    if (a > b and a<c) or (a<b and a>c) and a!=b and a!=c:
        return a
    elif (b>a and b<c) or (b<a and b >c)and b!=a and b!=c:
        return b
    else:
        return c

print(get_middle_value(-10,-10,-5))


