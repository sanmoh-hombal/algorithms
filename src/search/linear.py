from typing import Any, List


def search(input: List[Any], key: Any) -> bool:
    """
    :Linear Search:
    Search the input list for the key and return True if found, False otherwise.
    
    The function takes two arguments: input and key. The input argument is a list of any type, and the
    key argument is a single value of any type. The function returns a boolean value
    
    :param input: The list to search through
    :type input: List[Any]

    :param key: The value to search for in the input list
    :type key: Any

    :return: True or False
    """
    for item in input:
        if item == key:
            return True

    return False

sample_list = [2, 3, 4, 10, 40]
sample_key = 50
result: bool = search(input=sample_list, key=sample_key)
print(result)
