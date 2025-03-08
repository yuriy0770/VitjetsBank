import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    filename="../logs/mask.log",
    encoding="utf-8",
    filemode="w",
)

logger1 = logging.getLogger("mask1")
logger2 = logging.getLogger("mask2")


def get_mask_card_number(number_card: int) -> str:
    """ "Функция принимает на вход номер карты и возвращает ее маску"""
    logger1.info(f"Начало работы функции get_mask_card_number с номером карты {number_card}")

    if len(str(number_card)) != 16:
        logger1.error("Номер карты должен иметь 16 цифр")
        raise ValueError("Номер карты должен иметь 16 цифр")
    else:

        beyond_card = str(number_card)[:6] + "******" + str(number_card)[-4:]
        card_get = beyond_card[:4] + " " + beyond_card[4:8] + " " + beyond_card[8:12] + " " + beyond_card[12:]
        logger1.info(f"Функция get_mask_card_number завершила работу успешно. Маска номера карты: {card_get}")
        logger1.info(f"Зашершение работы функции")
        return card_get


def get_mask_account(number_score: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger2.info(f"Начало работы функции get_mask_account с номером карты {number_score}")
    if len(str(number_score)) != 16:
        logger2.error("Номер карты должен иметь 16 цифр")
        raise ValueError("Номер карты должен иметь 16 цифр")
    else:
        card_get1 = "**" + str(number_score)[-4:]
        logger1.info(f"Функция get_mask_card_number завершила работу успешно. Маска номера карты: {card_get1}")
        logger1.info(f"Зашершение работы функции")
        return card_get1


print(get_mask_card_number("6446584937585675"))
print(get_mask_account("6363636363636363"))
