import argparse
import logging
from bot.orders import OrderService
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Testnet)")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price, args.stop_price)

        service = OrderService()
        response = service.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price
        )

        print("Order Request Summary:")
        print(vars(args))

        print("\nOrder Response:")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        print("SUCCESS")

    except Exception as e:
        logging.error(str(e))
        print("FAILED:", str(e))

if __name__ == "__main__":
    main()
