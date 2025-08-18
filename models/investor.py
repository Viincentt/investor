from collections import defaultdict
import json
import os
from typing import Optional
import requests

from models.alpaca import Alpaca


class Investor:
    def __init__(self):
        self.alpaca = Alpaca()

        TICKERS = "TICKERS"
        with open("config.json") as f:
            data = json.load(f)
            amount = self.get_cash()
            self.d, total = defaultdict(float), 0
            for ticker, percentage in data[TICKERS].items():
                total += percentage
                self.d[ticker] = amount * (percentage / 100)
            if total != 100:
                raise ValueError("Not 100%")

    def get_cash(self):
        response: Optional[requests.Response] = self.alpaca.get_account()
        if response is None:
            return 0
        # TODO
        return 0

    def run(self):
        for ticker, amount_ in self.d.items():
            self.invest(ticker, amount_)

    def invest(self, ticker, amount):
        # limit buy
        print(f"Investing {amount} in {ticker}.")
        # TODO alpaca api call with self.key
