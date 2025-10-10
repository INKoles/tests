from typing import Union, Any, Optional

def get_uniq_list(list_1: list[Any], list_2: list[Any]) -> list[Any]:
    """Возвращает список, содержащий только числа,
    которые есть только в одном из списков
    """
    uniq_list = list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))

    return uniq_list


print(get_uniq_list([1, 2, 3, 4], [3, 4, 5, 6]))


def get_uniq_another(list_a: list[int], list_b: list[int]) -> list[int]:
    """ Возвращает список неповторяющихся чисел """
    uno_list: list[int] = []
    for i in list_a:
        if i not in list_b:
            uno_list.append(i)
    for i in list_b:
        if i not in list_a:
            uno_list.append(i)

    return uno_list


print(get_uniq_another([1, 2, 3, 4], [3, 4, 5, 6]))
