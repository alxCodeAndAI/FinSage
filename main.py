# -*- coding: utf-8 -*-
import pandas as pd
from Markets.stocks import Stock


def hello():
    return "hi"


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


if __name__ == "__main__":
    print(hello())

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
