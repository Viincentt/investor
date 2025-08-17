from collections import defaultdict
import json
import os


class Investor:
    def __init__(self):
        try:
            self.key = os.environ["ALPACA_KEY"]
        except:
            self.key = ""

        TICKERS = "TICKERS"
        with open("config.json") as f:
            data = json.load(f)
            amount = self.__get_cash()
            self.d, total = defaultdict(float), 0
            for ticker, percentage in data[TICKERS].items():
                total += percentage
                self.d[ticker] = amount * (percentage / 100)
            if total != 100:
                raise ValueError("Not 100%")

    def __get_cash(self):
        if not self.key:
            return 1000
        # TODO alpaca api call with self.key

    def run(self):
        for ticker, amount_ in self.d.items():
            self.__invest(ticker, amount_)

    def __invest(self, ticker, amount):
        # limit buy
        print(f"Investing {amount} in {ticker}.")
        # TODO alpaca api call with self.key
