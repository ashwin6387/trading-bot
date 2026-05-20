from binance.exceptions import BinanceAPIException
import logging

try:
    response = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=order_type,
        quantity=quantity
    )

    print("Order placed successfully!")
    print(response)

except BinanceAPIException as e:
    logging.error(f"Binance API Error: {e}")
    print(f"Binance API Error: {e}")

except Exception as e:
    logging.error(f"Unexpected Error: {e}")
    print(f"Unexpected Error: {e}")