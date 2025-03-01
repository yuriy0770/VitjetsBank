import pytest
from datetime import datetime
from src.decorators import log  # импортируем наш декоратор


def test_log_decorator_success(capfd):
    """Тест успешного логирования."""

    @log(filename="test_log.txt")
    def add(x, y):
        return x + y

    result = add(1, 2)

    captured = capfd.readouterr()
    assert "2023-03-10" in captured.out
    assert "Функция 'add' начата" in captured.out
    assert "Функция 'add' ok" in captured.out


def test_log_decorator_error(capfd):
    """Тест логирования ошибки."""

    @log(filename="test_log.txt")
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capfd.readouterr()
    assert "2023-03-10" in captured.out
    assert "Функция 'divide' начата" in captured.out
    assert "Функция 'divide' error: ZeroDivisionError: division by zero" in captured.out


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
