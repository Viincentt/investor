import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetAssetsRequest
from alpaca.trading.enums import OrderSide, TimeInForce, AssetClass, AssetStatus


class AlpacaAPI:
    def __init__(self) -> None:
        id_, secret = os.environ["ALPACA_ID"], os.environ["ALPACA_KEY"]
        self.client = TradingClient(id_, secret, paper=True)

    def get_account(self):
        return self.client.get_account()

    def market_buy(self, ticker, amount):
        order = MarketOrderRequest(
            symbol=ticker,
            notional=amount,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY,
        )
        return self.client.submit_order(order)
