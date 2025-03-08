from typing import Dict, Iterator, List


def filter_by_currency(transactions: Dict, id: str) -> Iterator:
    """Функция должна возвращать итератор,
    который поочередно выдает транзакции,
     где валюта операции соответствует заданной"""
    return (i for i in transactions if id in i["operationAmount"]["currency"]["name"])


def transaction_descriptions(transactions):
    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise ValueError("Некорректный формат входных данных")
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> str:
    """Генератор принимает начальное и конечное значения для генерации диапазона номеров."""
    for i in range(start, end + 1):
        yield f"{i:>016}"[:4] + " " + f"{i:>016}"[4:8] + " " + f"{i:>016}"[8:12] + " " + f"{i:>016}"[12:]
