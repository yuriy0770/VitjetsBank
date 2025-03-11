import csv
import logging
from typing import List
import pandas as pd



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                    filename="../logs/templates.log",
                    encoding="utf-8",
                    filemode="w")


logger1 = logging.getLogger("csv")
logger2 = logging.getLogger("excel")

def read_csv(csv_path: str) -> list:
    """Считывает csv файл и возврвщает срисок словарей"""
    logger1.info("начало работы функции")
    try:
        with open(csv_path, encoding="utf-8") as f:
            logger1.info("Считываем данные из файла csv")
            read_file = csv.reader(f, delimiter=";")
            f_str = next(read_file)
            list_row = []
            for i in read_file:
                dict_f = {}
                for j, k in enumerate(i):
                    dict_f[f_str[j]] = i[j]
                list_row.append(dict_f)
    except FileNotFoundError as ex:
        logger1.error(f"Ошибка {ex}")
        return 'Не правильно указан путь к файлу {ex}'
    else:
        logger1.info("Завершение работы")
        return list_row



def read_excel(excel_path: str) -> List:
    """Считывает excel файл и возврвщает срисок словарей"""
    try:
        logger2.info("начало работы функции")
        logger2.info("считываем данные из файла excel")
        q = pd.read_excel(excel_path)
        logger2.info("Создаем список строк")
        list_rows = q.values.tolist()
        logger2.info("Создаем список столбцов")
        list_col = list(q.columns)
        list_dict = []
        for i in list_rows:
            dict_f = {}
            for k, j in enumerate(list_col):
                dict_f[j] = i[k]
            list_dict.append(dict_f)
    except FileNotFoundError as ex:
        logger2.error(f"Ошибка {ex}")
        return []
    else:
        logger2.info("Возвращаем список словарей")
        logger2.info("Завершение работы")
        return list_dict











