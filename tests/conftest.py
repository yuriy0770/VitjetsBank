import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def get_mask_card_number1():
    return ["7001797779777364", "7001797779777364", "7001797779777368",
            "", "34534535", "8586585858958595858765", "76"]

@pytest.fixture
def get_mask_card_number3(get_mask_card_number1):
    list_card = []
    for i in get_mask_card_number1:
        if len(i) != 16:
            list_card.append("")
        else:
            beyond_card = str(i)[:6] + "******" + str(i)[-4:]
            list_card.append(beyond_card[:4] + " " + beyond_card[4:8] + " " + beyond_card[8:12] + " " + beyond_card[12:])
    return list_card





@pytest.fixture
def get_get_mask_account():
    return ["7000792289606361", "7001797779777364", "7001797779777364", "7001797779777368",
            "", "34534535", "8586585858958595858765", "76"]

@pytest.fixture
def get_mask_account1(get_get_mask_account):
    list_card1 = []
    for i in get_get_mask_account:
        if len(i) != 16:
            list_card1.append("")
        else:
            list_card1.append("**" + str(i)[-4:])
    return list_card1





@pytest.fixture
def mask_account_card11():
    return ["Visa Platinum 7000792289606361",
            'Maestro 1596837868705199',
            'Счет 64686473678894779589',
            'MasterCard 7158300734726758',
            'Счет 35383033474447895560',
            'Visa Classic 6831982476737658',
            'Visa Platinum 8990922113665229',
            'Visa Gold 5999414228426353',
            'Счет 73654108430135874305']


@pytest.fixture
def mask_account_card22(mask_account_card11):
    list_card2 = []
    for i in mask_account_card11:
        i = i.split()
        if i[0] == "Счет":
            list_card2.append(f'{i[0]} {get_mask_account(int(i[1]))}')
        else:
            list_card2.append(f'{" ".join(i[:-1])} {get_mask_card_number(int(i[-1]))}')
    return list_card2




@pytest.fixture
def get_date1():
    return ["2024-07-17T02:26:18.671407",
            "2022-06-29T02:26:18.671407",
            "2021-03-14T02:26:18.671407",
            "2024-02-22T02:26:18.671407"]

@pytest.fixture
def get_date2(get_date1):
    list_card3 = []
    for i in get_date1:
        list_card3.append(f'{i[8:10]}.{i[5:7]}.{i[:4]}')
    return list_card3