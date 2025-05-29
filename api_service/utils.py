import yfinance as yf

def get_stock_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        if not info:
            return {"error": "No data found for symbol"}
        return info
    except Exception as e:
        return {"error": str(e)}
