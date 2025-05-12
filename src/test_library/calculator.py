from .counter import Counter
from .divider import Divider
from .multiplier import Multiplier


class Calculator:
    """
    Class which encapsulates basic math operations
    """
    def __init__(self):
        self.counter = Counter()
        self.divider = Divider()
        self.multiplier = Multiplier()

    def add(self, a, b):
        self.counter.add(a, b)

    def divide(self, a, b):
        self.divider.divide(a, b)

    def mul(self, a, b):
        self.multiplier.mul(a, b)
