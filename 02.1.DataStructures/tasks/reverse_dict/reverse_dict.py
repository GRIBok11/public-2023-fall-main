import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    inverted_dict = dct(list)
    
    for key, value in d.items():
        inverted_dict[value].append(key)
    
    return dict(inverted_dict)

