import math
from typing import Any, List


def search(input: List[Any], key: Any) -> bool:
    """
    :Jump Search:
    We're going to take the square root of the length of the input list, and then we're going to
    iterate through the list in steps of the square root of the length of the input list, and if we find
    the key, we're going to return True, and if we don't find the key, we're going to return False
    
    :param input: The list of items to search through
    :type input: List[Any]

    :param key: The value we're searching for
    :type key: Any

    :return: A boolean value.
    """
    length: int = len(input)
    step: float = math.sqrt(length)
    previous: int = 0

    while input[int(min(step, length) - 1)] < key:
        previous = step
        step += math.sqrt(length)

        if previous >= length:
            return False
    
    while input[int(previous)] < key:
        previous += 1

        if previous == min(step, length):
            return False
    
    if input[int(previous)] == key:
        return True

sample_list = [2, 3, 4, 10, 40]
sample_key = 40
result: bool = search(input=sample_list, key=sample_key)
print(result)

