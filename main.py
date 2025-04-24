from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd


def hello():
    return "hi"


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


# Lista de tickers
tickers = [
    "BCOLOMBIA.CL",
    "BOGOTA.CL",
    "CELSIA.CL",
    "CEMARGOS.CL",
    "CNEC.CL",
    "CONCONCRET.CL",
    "CORFICOLCF.CL",
    "ECOPETROL.CL",
    "GEB.CL",
    "GRUPOSURA.CL",
    "ICOLCAP.CL",
    "ISA.CL",
    "NUTRESA.CL",
    "PFAVAL.CL",
    "PFBCOLOM.CL",
    "PFCEMARGOS.CL",
    "PFDAVVNDA.CL",
    "PFGRUPOARG.CL",
    "PFGRUPSURA.CL",
]

# Recolectar datos
all_data = []
for ticker in tickers:
    stock = Stock(ticker)
    historical_data = (
        stock.get_historical_prices()
    )  # Usa fechas calculadas dinámicamente
    if isinstance(historical_data, pd.DataFrame):
        all_data.append(historical_data)
    else:
        print(f"No se encontraron datos o hubo un error con el ticker {ticker}")

# Concatenar todos los datos en un único DataFrame
if all_data:
    combined_data = pd.concat(all_data, ignore_index=True)
    # Guardar como CSV
    output_file = "historical_prices.csv"
    combined_data.to_csv(output_file, index=False)
    print(f"Datos históricos guardados en {output_file}")
else:
    print("No se generaron datos para guardar.")
