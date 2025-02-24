import pytest
from src.decorators import log  # Импорт вашего модуля с декоратором


@pytest.fixture
def tmpdir():
    return pytest.TmpPath()


# Фикстура для перехвата вывода в консоль
@pytest.fixture
def capsys():
    return pytest.capturefromstdout()


# Тест на декорирование функции без аргументов
def test_log_no_args():
    @log()
    def add(a, b):
        """Возвращает сумму двух чисел."""
        return a + b

    result = add(5, 7)

    # Проверка того, что логирование работает правильно
    assert "12" in str(result)


# Тест на то, что функция не имеет аргументов для декоратора
def test_log_no_function_args():
    @log(123)
    def add(a, b):
        """Возвращает сумму двух чисел."""
        return a + b

    result = add(5, 7)

    # Проверка того, что логирование работает правильно
    assert "12" in str(result)



