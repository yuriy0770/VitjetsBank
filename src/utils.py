import json
import os
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    filename="../logs/utils.log",
    encoding="utf-8",
    filemode="w",
)

logger = logging.getLogger(__name__)


def load_financial_transactions(json_file_path):
    """Загружает данные о финансовых транзакциях из JSON-файла"""
    logger.info("Начало работы функции")
    if not os.path.exists(json_file_path):
        logger.info("Возвращаем пустой список так как не найден")
        logger.info("Зашершение функции")
        return []
    try:
        with open("../data/operations.json", encoding="utf-8") as file:
            logger.info(f"Выгружаем данные из файла {json_file_path.split('/')[-1]}")
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f"Ошибка {ex}")
        return []
    if not isinstance(data, list):
        logger.info("Возвращаем пустой список так тип данных у объекта не list")
        logger.info("Зашершение функции")
        return []
    transactions = []
    for item in data:
        if isinstance(item, dict):
            transactions.append(item)
    logger.info("Возвращаем список данных")
    logger.info("Зашершение функции")
    return transactions


print(load_financial_transactions("../data/operations.json"))
