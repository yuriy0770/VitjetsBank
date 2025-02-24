import pytest
from src.decorators import log  # Импорт вашего модуля с декоратором




def test_log_no_function_args():
    @log()
    def add1(a, b):
        return a / b

    assert add1(1, 2) == 'add1 ok'


def test_log1():
    @log(12)
    def add(a, b):
        return a + b

    with pytest.raises(ValueError, match='Не правильное название файла'):
        add(1, 2)


def test_log2():
    @log("efgeeg")
    def add(a, b):
        return a + b

    with pytest.raises(ValueError, match='Не правильное название файла'):
        add(1, 2)


def test_log3():
    @log("ughiug345636.,,.,.,")
    def add(a, b):
        return a + b

    with pytest.raises(ValueError, match='Не правильное название файла'):
        add(1, 2)


def test_log4():
    @log()
    def add(a, b):
        return a + b
    assert add(1, 2) == "add ok"


def test_log5(capsys):
    @log("example.txt")
    def add(a, b):
        return a+b

    assert add(1,2) == None

def test_log6(capsys):
    @log()
    def add(a, b):
        return a+b

    assert add('1',2) == f'add error: can only concatenate str (not "int") to str. Inputs: (\'1\', 2)'


