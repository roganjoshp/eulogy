import functools
from typing import Optional, List


class Config:
    def __init__(self):
        self.ignore_functions = False


def eulogise(tags: Optional[List] = None, config = Config()):
    def decorator(func):
        @functools.wraps(func)
        def add_function_log(*args, **kwargs):
            if not config.ignore_functions:
                print("MADE IT HERE")
                if tags is None:
                    print("HOW ABOUT NOW?")
            return func(*args, **kwargs)
        return add_function_log
    return decorator


@eulogise()
def test_function():
    a = 2


if __name__ == "__main__":
    test_function()