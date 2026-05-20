if order_type == "LIMIT" and not price:
    raise ValueError("Price required for LIMIT order")

if args.side not in ["BUY", "SELL"]:
    print("Invalid side")
    exit()

if args.type not in ["MARKET", "LIMIT"]:
    print("Invalid order type")
    exit()

if args.type == "LIMIT" and not args.price:
    print("LIMIT order requires price")
    exit()