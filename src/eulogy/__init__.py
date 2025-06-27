__version__ = "0.0.2"

from .config import Config
from .eulogy import _Eulogy

import atexit
import functools
import inspect


eulogy = _Eulogy()


def eulogise(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        module = inspect.getmodule(func).__name__
        eulogy.add(f"Function: {func.__name__} \t Module: {module}")
        return func(*args, **kwargs)

    return wrapper


atexit.register(eulogy.recite)
