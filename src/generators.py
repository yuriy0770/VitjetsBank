from typing import Dict, Iterator, List


def filter_by_currency(transactions: Dict, id: str) -> Iterator:
    """Функция должна возвращать итератор,
     который поочередно выдает транзакции,
      где валюта операции соответствует заданной"""
    return (i for i in transactions if id in i["operationAmount"]["currency"]["name"])


def transaction_descriptions(list_dict: List) -> str:
    '''принимает список словарей с транзакциями и возвращает описание каждой операции по очереди'''
    for i in list_dict:
        yield i["description"]


def card_number_generator(start: int, end: int) -> str:
    '''Генератор принимает начальное и конечное значения для генерации диапазона номеров.'''
    for i in range(start, end + 1):
        yield f'{i:>016}'[:4] + " " + f'{i:>016}'[4:8] + " " + f'{i:>016}'[8:12] + " " + f'{i:>016}'[12:]



