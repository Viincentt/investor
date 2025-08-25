from collections import defaultdict
import json

from models.alpaca_api import AlpacaAPI


class Investor:
    def __init__(self):
        self.alpaca = AlpacaAPI()

        TICKERS = "TICKERS"
        with open("config.json") as f:
            data = json.load(f)
            amount = self.get_cash()
            self.d, total = defaultdict(float), 0
            for ticker, percentage in data[TICKERS].items():
                total += percentage
                self.d[ticker] = amount * (percentage / 100)
            if total != 100:
                raise ValueError("Investments don't add up to 100%")

    def get_cash(self):
        res = self.alpaca.get_account().cash  # type: ignore
        return float(res) if res else 0

    def run(self):
        for ticker, amount_ in self.d.items():
            self.invest(ticker, amount_)

    def invest(self, ticker, amount):
        self.alpaca.market_buy(ticker, amount)
