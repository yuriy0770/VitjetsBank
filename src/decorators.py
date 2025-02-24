def log(filename=None):
    """Декоратор для автоматического логирования выполнения функций."""
    def wrapper(f):
        def inner(*args):
            if filename is not None and isinstance(filename, str) and filename[-3:] == "txt":
                try:
                    f(*args)
                except TypeError as f1:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{f.__name__} error: {f1}. Inputs: {args}")
                except ValueError as f1:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{f.__name__} error: {f1}. Inputs: {args}")
                else:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{f.__name__} ok")
            elif filename is None or filename == "":
                try:
                    f(*args)
                except TypeError as f2:
                    return f"{f.__name__} error: {f2}. Inputs: {args}"
                except ValueError as f2:
                    return f"{f.__name__} error: {f2}. Inputs: {args}"
                else:
                    return f"{f.__name__} ok"
            else:
                raise ValueError("Не правильное название файла")

        return inner
    return wrapper


