from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import generators


def tests_filter_by_currency(generators):
    q = filter_by_currency(generators, "USD")
    assert next(q) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                       'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                       'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                       'to': 'Счет 11776614605963066702'}
    assert next(q) == {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                       'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                       'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                       'to': 'Счет 75651667383060284188'}


def tests_transaction_descriptions(generators):
    w = transaction_descriptions(generators)
    assert next(w) == 'Перевод организации'
    assert next(w) == 'Перевод со счета на счет'
    assert next(w) == 'Перевод со счета на счет'
    assert next(w) == 'Перевод с карты на карту'
    assert next(w) == 'Перевод организации'


def tests_card_number_generator():
    e = card_number_generator(1, 5)
    assert next(e) == "0000 0000 0000 0001"
    assert next(e) == "0000 0000 0000 0002"
    assert next(e) == "0000 0000 0000 0003"
    assert next(e) == "0000 0000 0000 0004"
    assert next(e) == "0000 0000 0000 0005"
