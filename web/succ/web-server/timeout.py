# https://stackoverflow.com/questions/75928586/how-to-stop-the-execution-of-a-function-in-python-after-a-certain-time
from signal import signal, alarm, SIGALRM


class TimeoutError(Exception): ...


class Timeout:
    def __init__(self, seconds=1, message="Timed out"):
        self._seconds = seconds
        self._message = message

    @property
    def seconds(self):
        return self._seconds

    @property
    def message(self):
        return self._message

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, handler):
        self._handler = handler

    def handle_timeout(self, *_):
        raise TimeoutError(self.message)

    def __enter__(self):
        self.handler = signal(SIGALRM, self.handle_timeout)
        alarm(self.seconds)
        return self

    def __exit__(self, *_):
        alarm(0)
        signal(SIGALRM, self.handler)
