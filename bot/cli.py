import argparse
from orders import place_order

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

place_order(
    symbol=args.symbol,
    side=args.side,
    order_type=args.type,
    quantity=args.quantity,
    price=args.price
)