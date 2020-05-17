

class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._path = 'log.txt'

    def write(self, msg: str):
        with open(f'{self._path}', 'a') as f:
            f.write(f'{msg}\n')
