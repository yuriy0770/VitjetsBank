from typing import List


def filter_by_state(dict_lists: List, state='EXECUTED') -> List:
    '''Функция возвращает новый список словарей,
     содержащий только те словари, у которых ключ
     state соответствует указанному значению.'''
    return [i for i in dict_lists if state in list(i.values())]


def sort_by_date(dict_lists1: List, date=True) -> List:
    '''Функция возвращает новый список, отсортированный по date'''
    return sorted(dict_lists1, key=lambda x: x["date"], reverse=date)



