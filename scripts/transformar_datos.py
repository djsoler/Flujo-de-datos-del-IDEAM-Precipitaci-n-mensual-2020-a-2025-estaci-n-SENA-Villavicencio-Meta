import dask.dataframe as dd
import os

# Asegura que la carpeta 'salidas' exista
os.makedirs("C:/Users/JONANNA/Desktop/airflow/salidas", exist_ok=True)

# Lee el CSV de datos
df = dd.read_csv("C:/Users/JONANNA/Desktop/airflow/data/datos.csv")

# Asegúrate de que 'valor' es numérico
df["valor"] = df["valor"].astype(float)

# Filtra los valores mayores a 10
df_filtrado = df[df["valor"] > 10]

# Escribe los archivos filtrados (Dask crea múltiples archivos .part)
df_filtrado.to_csv("C:/Users/JONANNA/Desktop/airflow/salidas/filtrados-*.csv", index=False)
