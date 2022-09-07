from typing import Any, List


def search(input: List[Any], key: Any) -> bool:
    """
    :Binary Search:
    We start with the left and right pointers at the beginning and end of the list, respectively. We
    then move the left pointer to the right until it is at the first element that is greater than or
    equal to the key. We then move the right pointer to the left until it is at the first element that
    is less than or equal to the key. If the key is in the list, it will be at the left pointer
    
    :param input: List[Any] - the list of items to search through
    :type input: List[Any]

    :param key: The value we're searching for
    :type key: Any

    :return: True or False
    """
    left: int = 0
    right: int = len(input) - 1

    while right - left > 1:
        middle = (right + left) // 2
        if input[middle] < key:
            left = middle + 1
        else:
            right = middle
 
    if input[left] == key or input[right] == key:
       return True
    else:
        return False

sample_list = [2, 3, 4, 10, 40]
sample_key = 40
result: bool = search(input=sample_list, key=sample_key)
print(result)




