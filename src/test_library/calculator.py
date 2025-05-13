from .counter import Counter
from .divider import Divider
from .multiplier import Multiplier
from .substracter import Substracter


class Calculator:
    """
    Class which encapsulates basic math operations
    """
    def __init__(self):
        self.counter = Counter()
        self.divider = Divider()
        self.multiplier = Multiplier()
        self.substracter = Substracter()

    def add(self, a, b):
        self.counter.add(a, b)

    def divide(self, a, b):
        self.divider.divide(a, b)

    def mul(self, a, b):
        self.multiplier.mul(a, b)

    def sub(self, a, b):
        self.substracter.sub(a, b)

