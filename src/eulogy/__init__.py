__version__ = "0.0.2"

from .eulogy import Config, _Eulogy

import atexit
import functools
import inspect

from typing import List, Optional


eulogy = _Eulogy()


def eulogise(tags: Optional[List] = None):
    def decorator(func):
        @functools.wraps(func)
        def add_function_log(*args, **kwargs):
            if not eulogy.config.ignore_functions:
                module = inspect.getmodule(func).__name__
                log = f"Function: {module}.{func.__name__}"
                if tags is not None:
                    joined_tags = ", ".join(tags)
                    log = " ".join([log, "[TAGS]", joined_tags])
                eulogy.add(log)
            return func(*args, **kwargs)

        return add_function_log

    return decorator


atexit.register(eulogy.recite)
