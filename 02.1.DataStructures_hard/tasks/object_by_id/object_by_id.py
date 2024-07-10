import ctypes
import typing as tp

LONG_LEN = 8
INT_LEN = 4
CHAR_LEN = 1

ULONG_CHAR = "L" if ctypes.sizeof(ctypes.c_ulong) == 8 else "Q"
LONG_CHAR = "l" if ctypes.sizeof(ctypes.c_long) == 8 else "q"

def get_object_by_id(object_id: int) -> int | float | tuple[tp.Any, ...] | list[tp.Any] | str | bool:
    """
    Restores object by id.
    :param object_id: Object Id.
    :return: An object that corresponds to object_id.
    """
    # Получаем указатель на объект
    obj_ptr = ctypes.cast(object_id, ctypes.POINTER(ctypes.py_object))
    
    # Извлекаем объект
    obj = obj_ptr.contents.value
    
    return obj

# Пример использования
value = 37
restored_value = get_object_by_id(id(value))
print(restored_value)  # Вывод: 37
