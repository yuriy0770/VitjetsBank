from src.masks import get_mask_card_number, get_mask_account



def mask_account_card(card: str) -> str:
    """Функция, возвращающая замаскированный номер карты или счёта"""
    card1 = card.split()
    if card1[0] == "Счет":
        return f'{card1[0]} {get_mask_account(int(card1[1]))}'
    else:
        return f'{" ".join(card1[:-1])} {get_mask_card_number(int(card1[-1]))}'


def get_date(date: str) -> str:
    """возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return f'{date[8:10]}.{date[5:7]}.{date[:4]}'
