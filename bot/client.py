from binance.client import Client
from binance.exceptions import BinanceAPIException
import os
from dotenv import load_dotenv
from .logging_config import setup_logging

logger = setup_logging()

class BinanceFuturesClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_SECRET_KEY')
        
        if not api_key or not api_secret:
            raise ValueError("API Key and Secret must be set in .env file")
        
        self.client = Client(api_key, api_secret, testnet=True)
        logger.info("✅ Binance Futures Testnet client initialized")
    
    def get_account_balance(self, asset='USDT') -> dict:
        try:
            balance = self.client.futures_account_balance()
            for b in balance:
                if b['asset'] == asset:
                    return b
            return {}
        except Exception as e:
            logger.error(f"Failed to get balance: {e}")
            return {}
