from typing import List


def filter_by_state(dict_lists: List, state='EXECUTED') -> List:
    '''Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state

    сответствует указанному значению.'''
    for i in dict_lists:
        i["state"] = state
    return dict_lists


def sort_by_date(dict_lists: List, date=True) -> List:
    '''Функция должна возвращать новый список, отсортированный по дате'''
    return sorted(dict_lists, key=lambda x: x["date"], reverse=date)
