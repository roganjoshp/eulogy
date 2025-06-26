class Config:
    def __init__(
        self,
        max_log_length: int | None = 50,
        functions_only: bool = False,
        manual_only: bool = False,
        store_tracebacks: bool = True,
        timezone: str = "UTC",
    ) -> None:
        """Configuration of the core Eulogy logging functionality

        Parameters
        ----------
        max_log_length : int, optional
            Set a limit to the number of logged events being stored, covering
            both manual logs and function call traces, implemented as a deque,
            by default 50
        functions_only : bool
            Only store function call logged events and ignore manually logged
            events, by default False
        manual_only : bool
            Only store custom logged events and ignore logging of function
            calls, by default False
        store_tracebacks : bool
            Whether the full traceback should be stored in a log or whether to
            only store errors, by default True
        timezone : str
            The timezone of the logging timestamp, by default UTC
        """
        self.max_log_length = max_log_length
        self.functions_only = functions_only
        self.manual_only = manual_only
        self.store_tracebacks = store_tracebacks
        self.timezone = timezone
