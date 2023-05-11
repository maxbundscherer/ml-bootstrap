from dataclasses import dataclass


@dataclass
class SummaryItem:
    message: str


class SummaryText(SummaryItem):
    def __init__(self, message: str):
        super().__init__(message=message)


class SummaryAccuracy(SummaryItem):
    def __init__(self, identifier: str, accuracy: float):
        self.identifier: str = identifier
        self.accuracy: float = accuracy
        super().__init__(message=str(round(accuracy, 3)) + " by " + identifier)
