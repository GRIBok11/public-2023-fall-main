from collections.abc import Iterable, Iterator
from typing import Any


def flat_it(sequence: Iterable[Any]) -> Iterator[Any]:
    """
    :param sequence: iterable with arbitrary level of nested iterables
    :return: generator producing flatten sequence
    """
    for item in sequence:
        try:
            iter(item)
            if isinstance(item, (str, bytes)):
                yield item
            else:
                yield from flat_it(item)
        except TypeError:
            yield item
