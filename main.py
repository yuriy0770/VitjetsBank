import os

from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date, find_operations
from src.templates import read_csv, read_excel
from src.utils import load_financial_transactions


def path1():
    choice = input()
    if choice == "1":
        program_dir = os.path.join(os.path.dirname(__file__), 'data')
        absolute_json_file_path = os.path.join(program_dir, 'operations.json')
        return load_financial_transactions(absolute_json_file_path)
    elif choice == "2":
        program_dir = os.path.join(os.path.dirname(__file__), 'data')
        absolute_csv_file_path = os.path.join(program_dir, 'transactions.csv')
        return read_csv(absolute_csv_file_path)
    elif choice == "3":
        program_dir = os.path.join(os.path.dirname(__file__), 'data')
        absolute_excel_file_path = os.path.join(program_dir, 'transactions_excel.xlsx')
        return read_excel(absolute_excel_file_path)
    else:
        print(f'Нужно ввести одно число от 1 до 3')


def path2(path):
    categories = ['executed', 'canceled', 'pending']

    status_choice = input("Введите статус, по которому необходимо выполнить фильтрацию."
                          "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
    while status_choice.lower() not in categories:
        print(f"Статус операции '{status_choice}' недоступен.")
        status_choice = input("Введите статус, по которому необходимо выполнить фильтрацию. ")
    else:
        print(f'Операции отфильтрованы по статусу "{status_choice}"')
    return filter_by_state(path, status_choice)

def path3(pat1):
    sort_date = input("Отсортировать операции по дате? Да/Нет\n")
    if sort_date.lower() == "да":
        sort_by = input('Отсортировать по возрастанию или по убыванию?\n')
        if sort_by == 'по возрастанию':
            sorted_transactions = sort_by_date(pat1, False)
        elif sort_by == 'по убыванию':
            sorted_transactions = sort_by_date(pat1)
    else:
        sorted_transactions = pat1


    sort_by_rub = input('Выводить только рублевые тразакции? Да/Нет\n')
    if sort_by_rub.lower() == "да":
        so = filter_by_currency(sorted_transactions, "руб")
    elif sort_by_rub.lower() == 'нет':
        so = sorted_transactions

    filter = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n')
    if filter.lower() == "да":
        filter2 = input('Слово:')
        s = find_operations(so, filter2)
    elif filter.lower() == 'нет':
        s = so
    print('Распечатываю итоговый список транзакций...')
    if len(s) == 0:
         print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        open_resurs = [i for i in s if i["description"]=="Открытие вклада"]
        resurs = [i for i in s if i["description"]!="Открытие вклада"]
        print(f'Всего банковских операций в выборке: {len(s)-1}')
        print(f'{open_resurs[0]["date"][:10]} Открытие вклада ')
        print(f'''Счет {get_mask_account(open_resurs[0]['to'][-16:])}
Сумма: {open_resurs[0]['operationAmount']['amount']} {open_resurs[0]['operationAmount']['currency']['name']}''')
        for i in resurs:
            print(f'{i["date"][:10]} {i["description"]}\n'
                  f'{i['from'][:-16]+get_mask_card_number(i['from'][-16:])} -> {i['to']}\n'
                  f'Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}')



def main():

    path3(path2(path1()))




if __name__ == "__main__":
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    main()
