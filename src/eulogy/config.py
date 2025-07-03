from typing import Optional


class Config:
    def __init__(
        self,
        max_log_length: Optional[int] = 50,
        ignore_functions: bool = False,
        ignore_manual: bool = False,
        ignore_tracebacks: bool = False,
    ) -> None:
        """Configuration of the core Eulogy logging functionality

        Parameters
        ----------
        max_log_length : int, optional
            Set a limit to the number of logged events being stored, covering
            both manual logs and function call traces, implemented as a deque,
            by default 50
        ignore_functions : bool
            Prevent decorated functions from appearing in the log, by default
            False
        ignore_tracebacks : bool
            Prevent handled error tracebacks from appearing in the log, by 
            default False
        """
        self.max_log_length = max_log_length
        self.ignore_functions = ignore_functions
        self.ignore_manual = ignore_manual
        self.ignore_tracebacks = ignore_tracebacks
