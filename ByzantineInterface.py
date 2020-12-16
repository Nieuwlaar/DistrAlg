from abc import ABC

class ByzantineInterface(ABC):


    def __init__(self, other_generals):
        self.other_generals = other_generals


    def broadcast(self, message):
        pass