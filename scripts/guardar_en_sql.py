from sqlalchemy import create_engine
import pandas as pd

# Carga el archivo
df = pd.read_csv("/opt/airflow/salidas/predicciones.csv")

# Conexión a PostgreSQL (nombre del host es 'postgres')
engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")

# Guarda en SQL
df.to_sql("datos_guardados", engine, index=False, if_exists="replace")

print("Archivo cargado a la base de datos correctamente.")

