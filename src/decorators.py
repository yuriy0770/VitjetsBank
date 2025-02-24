import logging
from functools import wraps


def log(filename=None):
    """Декоратор для автоматического логирования выполнения функций."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                # Логирование результата успешной операции
                log_message = f"Функция '{func.__name__}' выполнена успешно. Результат: {result}"
                logging.info(log_message)

                return result

            except Exception as e:
                # Логирование ошибки, возникшей во время выполнения функции
                error_type = type(e).__name__
                log_message = f"Функция '{func.__name__}' завершилась с ошибкой {error_type}"
                logging.error(log_message)

                # Перехват и возврат исключения
                raise e

        return wrapper

    if filename is not None:
        # Создание файлового логера
        logging.basicConfig(filename=filename, level=logging.INFO)

    return decorator


# Пример использования декоратора:
@log(filename="example.log")
def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


print(add(5, 7))

