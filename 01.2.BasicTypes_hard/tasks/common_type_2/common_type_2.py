import typing as tp


def convert_to_common_type(data: list[tp.Any]) -> list[tp.Any]:
    """
    Takes list of multiple types' elements and convert each element to common type according to given rules
    :param data: list of multiple types' elements
    :return: list with elements converted to common type
    """
    common_type = None  # Initialize with None (unknown type)

    # Determine the common type based on the input values
    for val in data:
        if val is None or val == "":
            continue  # Skip unknown values
        elif isinstance(val, (list, tuple)):
            common_type = list  # Use list type
        elif isinstance(val, int):
            common_type = int  # Use int type
        elif isinstance(val, float):
            common_type = float  # Use float type
        elif isinstance(val, bool):
            common_type = bool  # Use bool type
        elif isinstance(val, str):
            common_type = str  # Use str type
            break  # If we find a string, no need to check further

    # Convert all values to the determined common type
    converted_values = []
    for val in data:
        if val is None or val == "":
            converted_values.append(common_type())  # Use default value
        else:
            converted_values.append(common_type(val))

    return converted_values

