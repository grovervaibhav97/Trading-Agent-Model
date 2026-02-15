import pandas as pd

class TradingEnvironment:
    def __init__(self, file):
        self.data = pd.read_csv(file)
        self.prices = self.data['price'].values
        self.reset()

    def reset(self):
        self.index = 0
        self.balance = 10000
        self.shares = 0
        self.net_worth = self.balance
        return self.prices[self.index]

    def step(self, action):
        price = self.prices[self.index]

        if action == 1 and self.balance >= price:
            self.shares += 1
            self.balance -= price

        elif action == 2 and self.shares > 0:
            self.shares -= 1
            self.balance += price

        self.index += 1
        done = self.index == len(self.prices) - 1

        self.net_worth = self.balance + self.shares * price
        reward = self.net_worth

        return self.prices[self.index], reward, done
