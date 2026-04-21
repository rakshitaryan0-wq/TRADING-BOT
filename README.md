# 🚀 Binance Futures Trading Bot

**MARKET & LIMIT orders on Binance Testnet USDT-M Futures**

## 🚀 Quick Start

1. **Get Testnet API Keys:** https://testnet.binancefuture.com
2. **Copy `.env.example` → `.env`** and add keys
3. **Install:** `pip install -r requirements.txt`
4. **Run:**
```bash
python run.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
python run.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 45000

📁 Structure

Copy code
.gitignore     Security
.env.example   Template  
requirements.txt
bot/           6 modules
run.py         Entry point
logs/          Auto-logs

✅ Proof
[ ] MARKET order screenshot
[ ] LIMIT order screenshot
[ ] Logs in logs/

Copy code

---

## **🎯 EXECUTE THIS ORDER:**

```bash
# 1. Folder structure
mkdir -p trading_bot/{bot,logs,screenshots} && cd trading_bot

# 2-12. Create files above IN ORDER (copy each content)

# 13. Install & test
pip install -r requirements.txt
cp .env.example .env  # Edit with YOUR NEW KEYS
python run.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

# 14. Git (SAFE!)
git init && git add . && git commit -m "Complete bot" && git push

✅ TEST COMMANDS (Take Screenshots)

python run.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
python run.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 45000

## 🔐 Security Notes

⚠️ **NEVER commit `.env` to GitHub!**
