__version__ = "0.0.2"

from .eulogy import Config, _Eulogy

import atexit
import functools
import inspect

from typing import List, Optional


eulogy = _Eulogy()


def eulogise(tags: Optional[List] = None, config=Config()):
    """Decorator to log function calls, with optional additional tags

    _extended_summary_

    Parameters
    ----------
    tags : _type_, optional
        _description_, by default None
    """

    def decorator(func):
        @functools.wraps(func)
        def add_function_log(*args, **kwargs):
            if not config.ignore_functions:
                module = inspect.getmodule(func).__name__
                eulogy.add(f"Function: {module}.{func.__name__}")
            return func(*args, **kwargs)

        return add_function_log

    return decorator


atexit.register(eulogy.recite)
