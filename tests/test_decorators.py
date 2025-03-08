from fileinput import filename

import pytest

from src.decorators import log  # импортируем наш декоратор


def test_log():
    """Тест на сложение"""

    @log()
    def add(a, b):
        return a + b

    assert add(1, 2) == 3


def test_log2():
    """Тест на умножение"""

    @log()
    def q(a, b):
        return a * b

    assert q(2, 3) == 6


def test_log3():
    """Тест на деление"""

    @log()
    def q(a, b):
        return a / b

    assert q(10, 2) == 5.0


def test_log4():
    """Тест на вычитание"""

    @log()
    def q(a, b):
        return a - b

    assert q(10, 2) == 8


def test_log_decorator_no_file_name(capfd):
    """Тест логирования без файла."""

    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)

    captured = capfd.readouterr()
    assert "Функция 'my_function' начата" in captured.out
    assert "Функция 'my_function' ok" in captured.out


def test_log_decorator_error_no_file_name(capfd):
    """Тест логирования ошибки без файла."""

    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capfd.readouterr()
    assert "Функция 'divide' начата" in captured.out
    assert "Функция 'divide' error: ZeroDivisionError: division by zero" in captured.out


def test_log_decorator_success(capfd):
    """Тест успешного логирования."""

    @log(filename="test_log.txt")
    def add(x, y):
        return x + y

    result = add(1, 2)

    captured = capfd.readouterr()
    assert "Функция 'add' начата" not in captured.out
    assert "Функция 'add' ока" not in captured.out


def test_log_decorator_success_output(capfd):
    """Тест успешного логирования с проверкой вывода."""

    @log(filename="test_log.txt")
    def add(x, y):
        return x + y

    result = add(1, 2)

    captured = capfd.readouterr()

    assert "Функция 'add' начата\n2023-03-10 15:00:00: Функция 'add' ока" not in captured.out


def test_log_decorator_error(capfd):
    """Тест логирования ошибки."""

    @log(filename="test_log.txt")
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capfd.readouterr()
    assert "Функция 'divide' ока\n2023-03-10 15:00:00: Функция 'divide' error: ZeroDivisionError: division by zero" not in captured.out