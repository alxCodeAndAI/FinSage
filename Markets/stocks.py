from datetime import datetime, timedelta
import yfinance as yf

class Stock:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.stock = yf.Ticker(self.ticker_symbol)

    def get_historical_prices(self, start=None, end=None, interval="1d"):
        try:
            if not start:
                start = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
            if not end:
                end = datetime.now().strftime("%Y-%m-%d")

            data = self.stock.history(start=start, end=end, interval=interval)
            if data.empty:
                return None
            data.reset_index(
                inplace=True
            )  # Asegurar que las fechas estén como columnas
            data["Ticker"] = self.ticker_symbol  # Agregar el ticker a los datos
            return data
        except Exception as e:
            return f"Error al obtener datos para {self.ticker_symbol}: {e}"
