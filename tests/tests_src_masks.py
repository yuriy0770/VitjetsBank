import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number1():
    assert get_mask_card_number("1234746532784873") == "1234 74** **** 4873"

def test_get_mask_card_number2():
    assert get_mask_card_number("1234746532787773") == "1234 74** **** 7773"

def test_get_mask_card_number3():
    assert get_mask_card_number("7734746532784873") == "7734 74** **** 4873"
    assert get_mask_card_number("7734746532785555") == "7734 74** **** 5555"
    assert get_mask_card_number("1111746532784873") == "1111 74** **** 4873"
    assert get_mask_card_number("5555746532782222") == "5555 74** **** 2222"

def test_get_mask_card_number2():
    with pytest.raises(Exception):
        get_mask_card_number("345453")
    with pytest.raises(Exception):
        get_mask_card_number("")
    with pytest.raises(Exception):
        get_mask_card_number("564766767757657575757")



@pytest.mark.parametrize("test1, test2", [("7000792289606361", "**6361"),
                                          ("7001797779777364", "**7364"),
                                          ("7001797779777377", "**7377"),
                                          ("9999797779777355", "**7355"),
                                          ("5555797779777444", "**7444")])
def tests_get_mask_account1(test1, test2):
    assert get_mask_account(test1) == test2


def test_get_mask_account2():
    with pytest.raises(Exception):
        get_mask_card_number("34543")
    with pytest.raises(Exception):
        get_mask_card_number("")
    with pytest.raises(Exception):
        get_mask_card_number("56476676774564657657575757")