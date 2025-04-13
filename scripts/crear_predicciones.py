import pandas as pd

# Ruta de entrada
df = pd.read_csv("C:/Users/JONANNA/Desktop/airflow/descargaDhime.csv")

# Selección y renombramiento de columnas
df_simple = df[["Fecha", "Valor"]].copy()
df_simple.columns = ["fecha", "valor"]

# Conversión de fechas
df_simple["fecha"] = pd.to_datetime(df_simple["fecha"]).dt.strftime("%Y-%m-%d")

# Guardar como predicciones.csv en carpeta 'salidas'
df_simple.to_csv("salidas/predicciones.csv", index=False)

print("Archivo predicciones.csv creado exitosamente.")


