import pytest

from src.widget import mask_account_card, get_date


def tests_mask_account_card1(mask_account_card1):
    assert mask_account_card(mask_account_card1) == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 7365410843014305") == "Счет **4305"


def test_mask_account_card2():
    with pytest.raises(Exception):
        mask_account_card("345453")
    with pytest.raises(Exception):
        mask_account_card("")
    with pytest.raises(Exception):
        mask_account_card("564766767757657575757")


@pytest.mark.parametrize(
    "test1, test2",
    [
        ("2024-09-11T02:26:18.671407", "11.09.2024"),
        ("2027-11-11T02:26:18.671407", "11.11.2027"),
        ("2024-09-11T02:26:18.671407", "11.09.2024"),
        ("2024-03-22T02:26:18.671407", "22.03.2024"),
    ],
)
def tests_get_date(test1, test2):
    assert get_date(test1) == test2
