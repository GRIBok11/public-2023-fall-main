def get_common_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """
    if type2==range and type1==range:
        return tuple
    if type1 == type2 :
        return type1
    if type1 == str or type2 ==str:
        return str
    elif (type1 == tuple or type2 == tuple) and (type2==list or type1==list):
        return list
    elif (type1 == tuple or type2 == tuple) and (type1==range or type2==range or type2==list or type1==list)or (type1==tuple and type2== tuple):
        return tuple 
    elif (type1 == list or type2 == list) and (type1==range or type2==range):
        return list
    elif type2==list or type2 == range or type2==tuple or type1 == list or type1 == range or type1==tuple:
        return str
    elif type1== complex or type2 == complex:
        return complex
    elif type1== float or type2==float:
        return float
    elif type1==int or type2 == int:
        return int

    return type2