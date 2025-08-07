class Strategy:
    def __init__(self, key, amount=0):
        self.amount = amount
        self.__key = key

    def invest(self):
        raise NotImplementedError()


class MyETF(Strategy):
    def __init__(self, amount):
        # open config.json
        # keep list of companies with resp. percentages
        # update Strategy(with key and amount)
        super(amount)
        """
        {
            "AAPL": 1000 -> 33.3
            "MSFT": 1000 -> 33.3
            "GOOG": 1000 -> 33.3
            "GME": 1 -> 0.000001
        }
        """

    def invest(self):
        pass


def main():
    amount = 0
    strategies = [MyETF(amount)]
    for strategy in strategies:
        strategy.invest()
