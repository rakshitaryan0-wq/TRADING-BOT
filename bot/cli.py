import argparse
import sys
from .client import BinanceFuturesClient
from .orders import OrderManager
from .validators import validate_inputs
from .logging_config import setup_logging

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="🚀 Binance Futures Trading Bot")
    parser.add_argument('--symbol', required=True, help="e.g., BTCUSDT")
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'])
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument('--qty', '--quantity', required=True, type=str)
    parser.add_argument('--price', type=str)
    
    args = parser.parse_args()
    
    is_valid, message = validate_inputs(args.symbol, args.side, args.type, args.qty, args.price)
    if not is_valid:
        print(f"❌ {message}")
        sys.exit(1)
    
    try:
        client = BinanceFuturesClient()
        order_mgr = OrderManager(client)
        
        balance = client.get_account_balance()
        print(f"💰 USDT Balance: {balance.get('balance', 'N/A')}")
        
        if args.type.upper() == 'MARKET':
            order = order_mgr.place_market_order(args.symbol, args.side, float(args.qty))
        else:
            order = order_mgr.place_limit_order(args.symbol, args.side, float(args.qty), float(args.price))
        
        order_mgr.print_order_summary(order, args.type, args.symbol, args.side, float(args.qty), 
                                    float(args.price) if args.price else None)
        
    except Exception as e:
        logger.error(f"💥 Failed: {e}")
        print(f"💥 Failed: {e}")
        sys.exit(1)
