import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import generators


def tests_filter_by_currency(generators):
    test = filter_by_currency(generators, "USD")
    assert next(test) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(test) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def tests_transaction_descriptions(generators):
    test2 = transaction_descriptions(generators)
    assert next(test2) == "Перевод организации"
    assert next(test2) == "Перевод со счета на счет"
    assert next(test2) == "Перевод со счета на счет"
    assert next(test2) == "Перевод с карты на карту"
    assert next(test2) == "Перевод организации"


def tests_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [{"id": 1, "description": "Перевод организации"}, {"id": 2, "description": "Перевод со счета на счет"}],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
        ([{"id": 3, "description": "Тестовый описания"}], ["Тестовый описания"]),
    ],
)
def test_transaction_descriptions(transactions, expected):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected


def test_transaction_descriptions_no_description():
    transactions = [{"id": 1}, {"id": 2}]
    with pytest.raises(KeyError):
        list(transaction_descriptions(transactions))


def test_transaction_descriptions_empty_description():
    transactions = [{"description": ""}, {"description": None}, {}]
    descriptions = [next(transaction_descriptions(transactions)) for _ in range(3)]
    assert all(description == "" or description is None for description in descriptions)
