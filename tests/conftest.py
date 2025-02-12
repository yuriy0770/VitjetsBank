import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def get_mask_card_number1():
    return ["7001797779777364", "7001797779777364", "7001797779777368",
            "", "34534535", "8586585858958595858765", "76"]

@pytest.fixture
def get_mask_account():
    return ["7000792289606361", "7001797779777364", "7001797779777364", "7001797779777368",
            "", "34534535", "8586585858958595858765", "76"]

@pytest.fixture
def mask_account_card1():
    return "Visa Platinum 7000792289606361"



@pytest.fixture
def get_date():
    return ["2024-07-17T02:26:18.671407",
            "2022-06-29T02:26:18.671407",
            "2021-03-14T02:26:18.671407",
            "2024-02-22T02:26:18.671407"]
@pytest.fixture
def filter_by_state_open():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def filter_by_state_exit1():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def filter_by_state_exit2():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def sort_by_date_open():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def sort_by_date_exit():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]