import json
from typing import List


class Investor:
    def __init__(self):
        self.strategies: List[Strategy] = []
        strategy_names = {"ETF": Etf}
        with open("config.json") as f:
            data = json.load(f)
            key = data["ALPACA_API_KEY"]
            amount = self.__get_cash(key) / len(strategy_names)
            for name, strategy_data in data["STRATEGIES"].items():
                self.strategies.append(strategy_names[name](key, amount, strategy_data))

    def __get_cash(self, key):
        return 100  # TODO

    def run_strategies(self):
        for strategy in self.strategies:
            strategy.invest()


class Strategy:
    def __init__(self, key, amount):
        self.key = key
        self.amount = amount

    def invest(self):
        raise NotImplementedError()

    def limit_buy(self, ticker, amount):
        # TODO
        print(f"Buying {amount} USD of {ticker}")


class Etf(Strategy):
    def __init__(self, key, amount, data):
        super().__init__(key, amount)
        self.companies = data["COMPANIES"]

    def invest(self):
        amount_to_invest = self.amount / len(self.companies)
        for company in self.companies:
            self.limit_buy(company, amount_to_invest)
