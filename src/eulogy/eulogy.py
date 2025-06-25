import os
import traceback

from collections import deque
from contextlib import redirect_stderr


class _Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = (
                super(_Singleton, cls).__call__(*args, **kwargs)
            )
        return cls._instances[cls]
    

class _Eulogy(metaclass=_Singleton):
    
    def __init__(self, maxlen=None):
        self._epitaph = deque(maxlen=maxlen)
    
    def add(self, 
            item: str):
        self._epitaph.append(item)
        
    def recite(self, 
               force: bool = False):
        """ Prints the contents of the log

        Parameters
        ----------
        force : bool, optional
            When set to True, the contents can be printed on demand, 
            by default False
        """
        
        if force and not self._epitaph:
            print("No eulogy to print")
        
        if self._epitaph:
            try:
                if not force:
                    with open(os.devnull, 'w') as f:
                        with redirect_stderr(f):
                            traceback.print_last()
                print()
                print("##### EULOGY RECITAL #####")
                for row in self._epitaph:
                    print(row)
            except ValueError:
                pass