def get_mask_card_number(number_card: int) -> str:
    """ "Функция принимает на вход номер карты и возвращает ее маску"""
    if len(str(number_card)) != 16:
        raise ValueError("Номер карты должен иметь 16 цифр")
    else:
        beyond_card = str(number_card)[:6] + "******" + str(number_card)[-4:]
        return beyond_card[:4] + " " + beyond_card[4:8] + " " + beyond_card[8:12] + " " + beyond_card[12:]


def get_mask_account(number_score: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(str(number_score)) != 16:
        raise ValueError("Номер карты должен иметь 16 цифр")
    else:
        return "**" + str(number_score)[-4:]
