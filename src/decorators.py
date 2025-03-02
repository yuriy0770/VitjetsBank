import functools
from datetime import datetime


def log(filename=None):
    """Декоратор для автоматического логирования выполнения функций."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Начало логирования
                if filename is not None:
                    with open(filename, "a", encoding='utf-8') as f:
                        log_message = f"{datetime.now()}: Функция '{func.__name__}' начата\n"

                        f.write(log_message)
                else:
                    print(f"Функция '{func.__name__}' начата")

                # Выполнение функции
                result = func(*args, **kwargs)

                # Логирование результата успешной операции
                if filename is not None:
                    with open(filename, "a", encoding='utf-8') as f:
                        log_message = f"{datetime.now()}: Функция '{func.__name__}' ok\n"

                        f.write(log_message)
                else:
                    print(f"Функция '{func.__name__}' ok")

                return result

            except Exception as e:
                # Логирование ошибки, возникшей во время выполнения функции
                if filename is not None:
                    with open(filename, "a", encoding='utf-8') as f:
                        log_message = (
                                f"{datetime.now()}: "
                                + f"Функция '{func.__name__}' error: {type(e).__name__}: {str(e)}\n"
                        )

                        f.write(log_message)
                else:
                    print(
                        f"Функция '{func.__name__}' error: {type(e).__name__}: {str(e)}"
                    )

                # Перехват и возврат исключения
                raise e

        return wrapper

    return decorator


