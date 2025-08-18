import os
import requests


class Alpaca:
    def __init__(self) -> None:
        try:
            self.headers = {
                "accept": "application/json",
                "APCA-API-KEY-ID": os.environ["ALPACA_ID"],
                "APCA-API-SECRET-KEY": os.environ["ALPACA_KEY"],
            }
        except:
            self.headers = {}

    def check_status(self, response: requests.Response):
        if response.status_code != 200:
            raise ConnectionError("Request response return code failed.")

    def get_account(self):
        url = "https://paper-api.alpaca.markets/v2/account"
        if not self.headers:
            return None
        response = requests.get(url, headers=self.headers)
        self.check_status(response)
        return response.json()
