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


def count_operations_by_category(operations: list[dict], categories: list[str], category=None) -> dict:
    # Инициализируем словарь результатов
    results = {category: 0 for category in categories}

    # Проходимся через каждую операцию
    for operation in operations:
        # Проверяем, содержит ли описание операции любое из категорий
        if any(category in operation["description"] for category in categories):
            # Если да - увеличиваем счетчик для этой категории
            results[category] += 1

    # Возвращаем словарь результатов
    return results
