import os
import traceback

import datetime as dt

from collections import deque
from contextlib import redirect_stderr
from typing import Optional

from .config import Config


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class _Eulogy(metaclass=_Singleton):
    def __init__(self):
        self.config = Config()
        self._epitaph = deque(maxlen=self.config.max_report_length)
        
    def set_config(self, config: Config):
        self.config = config
        # Since the class was instantiated with a deque already,
        # we might need to copy over the existing log here and
        # truncate to the new length
        self._epitaph.rotate(config.max_report_length)
        old_epitaph = list(self._epitaph)[:config.max_report_length]
        new_epitaph = deque(maxlen=self.config.max_report_length)
        for item in old_epitaph:
            new_epitaph.append(item)
        self._epitaph = new_epitaph

    def add(self, item: str):
        if not self.config.ignore_manual:
            self._epitaph.append(
                f"[{dt.datetime.now(dt.timezone.utc)}] " + item
            )

    def add_tb(self):
        if not self.config.ignore_tracebacks:
            self._epitaph.append(
                f"[{dt.datetime.now(dt.timezone.utc)}]\n"
                + traceback.format_exc()
            )

    def recite(self, force: bool = False):
        """Prints the contents of the log

        Parameters
        ----------
        force : bool, optional
            When set to True, the contents can be printed on demand without any
            traceback, by default False
        """

        if force and not self._epitaph:
            print("No eulogy to print")

        if self._epitaph:
            try:
                if not force:
                    with open(os.devnull, "w") as f:
                        with redirect_stderr(f):
                            traceback.print_last()
                print()
                print("--- RECITAL ---")
                for row in self._epitaph:
                    print(row)
            except ValueError:
                # Error stack is empty so ignore logged events
                pass
