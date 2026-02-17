import logging
from bot.client import BinanceFuturesClient

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        logging.info(f"Request: {symbol} {side} {order_type} {quantity} {price} {stop_price}")

        params = {
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
        }

        if order_type == "MARKET":
            params["type"] = "MARKET"

        elif order_type == "LIMIT":
            params["type"] = "LIMIT"
            params["price"] = price
            params["timeInForce"] = "GTC"

        elif order_type == "STOP_LIMIT":
            params["type"] = "STOP"
            params["price"] = price
            params["stopPrice"] = stop_price
            params["timeInForce"] = "GTC"

        response = self.client.create_order(**params)

        logging.info(f"Response: {response}")
        return response
