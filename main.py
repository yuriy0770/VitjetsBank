import time


def wrapper(f):
    def inner(*args):
        return f(*args)*3
    return inner

@wrapper
def q(w, e):
    return w + e

print(q(1, 2))