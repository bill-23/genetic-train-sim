
class TrainSimError(Exception):
    def __init__(self, msg: str = None):
        if msg:
            self.message = msg
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"TrainSimError {self.message}"
        else:
            return "TrainSimError raised"


class TrainSimInvalidInputError(TrainSimError):
    def __init__(self, msg: str = None):
        super().__init__(msg)