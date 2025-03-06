import json
import os


def load_financial_transactions(json_file_path):
    """Загружает данные о финансовых транзакциях из JSON-файла"""
    if not os.path.exists(json_file_path):
        return []
    try:
        with open("data/operations.json", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    if not isinstance(data, list):
        return []
    transactions = []
    for item in data:
        if isinstance(item, dict):
            transactions.append(item)

    return transactions


print(load_financial_transactions("data/operations.json"))
