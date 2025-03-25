import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import generators


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
