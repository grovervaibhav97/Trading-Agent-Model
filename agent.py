import random

class TradingAgent:
    def __init__(self):
        self.actions = [0, 1, 2]

    def act(self):
        return random.choice(self.actions)
