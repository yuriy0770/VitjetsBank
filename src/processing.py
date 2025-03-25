from collections import Counter
from typing import List
import re


def filter_by_state(dict_lists: List, state: str = "EXECUTED") -> List:
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    return [i for i in dict_lists if i.get("state") == state]


def sort_by_date(dict_lists1: List, descending: bool = True) -> List:
    """Функция возвращает новый список, отсортированный по date"""
    return sorted(dict_lists1, key=lambda x: x["date"], reverse=descending)


def find_operations(operations: list[dict], search_string: str) -> list[dict]:
    # Преобразуем строку поиска в регулярное выражение
    pattern = re.escape(search_string)

    # Инициализируем список результатов
    results = []

    # Проходимся через каждую операцию
    for operation in operations:
        # Проверяем, содержит ли описание операции данную строку поиска
        if re.search(pattern, operation["description"], re.IGNORECASE):
            # Если да - добавляем операцию в результаты
            results.append(operation)

    # Возвращаем список результатов
    return results



def count_operations_by_category(operations: list[dict], categories: list[str]) -> dict:
    # Состояние описаний операций в виде строки
    descriptions = ' '.join(operation["description"] for operation in operations)

    # Подсчет категорий в описаниях операций
    category_counts = Counter(category for description in (operation["description"] for operation in operations)
                              if any(category in description for category in categories) for category in categories)

    return dict(category_counts)