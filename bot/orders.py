from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from typing import Dict, Any
from .logging_config import setup_logging

logger = setup_logging()

class OrderManager:
    def __init__(self, client):
        self.client = client
    
    def place_market_order(self, symbol: str, side: str, quantity: float) -> Dict[str, Any]:
        logger.info(f"📈 Placing MARKET {side} order for {symbol}: {quantity}")
        try:
            order = self.client.futures_create_order(
                symbol=symbol, side=side, type='MARKET', quantity=quantity
            )
            logger.info(f"✅ MARKET order placed: {order['orderId']}")
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"❌ Order error: {e}")
            raise
    
    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> Dict[str, Any]:
        logger.info(f"📈 Placing LIMIT {side} order for {symbol}: {quantity} @ {price}")
        try:
            order = self.client.futures_create_order(
                symbol=symbol, side=side, type='LIMIT', 
                timeInForce='GTC', quantity=quantity, price=price
            )
            logger.info(f"✅ LIMIT order placed: {order['orderId']}")
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"❌ Order error: {e}")
            raise
    
    def print_order_summary(self, order: Dict[str, Any], order_type: str, symbol: str, 
                          side: str, quantity: float, price: float = None):
        print("\n" + "="*60)
        print("📊 ORDER EXECUTION SUMMARY")
        print("="*60)
        print(f"Symbol:     {symbol}")
        print(f"Side:       {side}")
        print(f"Type:       {order_type}")
        print(f"Quantity:   {quantity}")
        if price: print(f"Price:      ${price:,.2f}")
        print("-"*60)
        print("RESPONSE:")
        print(f"Order ID:   {order.get('orderId', 'N/A')}")
        print(f"Status:     {order.get('status', 'N/A')}")
        print(f"Executed:   {order.get('executedQty', 'N/A')}")
        print(f"Avg Price:  {order.get('avgPrice', 'N/A')}")
        print("="*60)
