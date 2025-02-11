import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date
from tests.conftest import get_get_mask_account


def tests_get_mask_card_number(get_mask_card_number1, get_mask_card_number3):
    for i in range(5):
        assert get_mask_card_number(get_mask_card_number1[i]) == get_mask_card_number3[i]


def tests_get_mask_account(get_get_mask_account, get_mask_account1):
    for i in range(8):
        assert get_mask_account(get_get_mask_account[i]) == get_mask_account1[i]


def tests_mask_account_card(mask_account_card11, mask_account_card22):
    for i in range(9):
        assert mask_account_card(mask_account_card11[i]) == mask_account_card22[i]


def tests_get_date(get_date1, get_date2):
    for i in range(4):
        assert get_date(get_date1[i]) == get_date2[i]


@pytest.mark.parametrize("test1, test2", [("2024-03-11T02:26:18.671407", '11.03.2024'),
                                          ("2024-03-21T02:26:18.671407", '21.03.2024'),
                                          ("2024-07-31T02:26:18.671407", '31.07.2024')])
def test_get_date(test1, test2):
    assert get_date(test1) == test2


def test_filter_by_state():
    assert (filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], ) ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
    assert (filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                            'CANCELED') ==
            [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])


def test_sort_by_date():
    assert (sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
