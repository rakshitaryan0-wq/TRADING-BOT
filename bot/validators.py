import re
from typing import Optional

def validate_symbol(symbol: str) -> bool:
    pattern = r'^[A-Z0-9]{6,12}$'
    return bool(re.match(pattern, symbol))

def validate_side(side: str) -> bool:
    return side.upper() in ['BUY', 'SELL']

def validate_quantity(qty: str) -> bool:
    try:
        q = float(qty)
        return q > 0
    except ValueError:
        return False

def validate_price(price: str) -> bool:
    try:
        p = float(price)
        return p > 0
    except ValueError:
        return False

def validate_order_type(order_type: str) -> bool:
    return order_type.upper() in ['MARKET', 'LIMIT']

def validate_inputs(symbol: str, side: str, order_type: str, qty: str, price: Optional[str] = None) -> tuple[bool, str]:
    if not validate_symbol(symbol):
        return False, "Invalid symbol. Use format like BTCUSDT"
    if not validate_side(side):
        return False, "Side must be BUY or SELL"
    if not validate_order_type(order_type):
        return False, "Order type must be MARKET or LIMIT"
    if not validate_quantity(qty):
        return False, "Quantity must be a positive number"
    if order_type.upper() == 'LIMIT' and (not price or not validate_price(price)):
        return False, "Price must be provided and positive for LIMIT orders"
    return True, "Valid"
