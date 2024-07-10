import typing as tp
from collections import defaultdict

def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    inverted_dict = defaultdict(list)
    
    for key, value in dct.items():
        inverted_dict[value].append(key)
    
    return dict(inverted_dict)

