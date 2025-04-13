"""
Este script entrena un modelo de regresión lineal usando datos de precipitación mensual total
obtenidos del IDEAM para el periodo 2020-2025. La información corresponde a la ciudad de Villavicencio,
Departamento del Meta, punto de medición o estación: SENA.

Fuente: IDEAM - Instituto de Hidrología, Meteorología y Estudios Ambientales de Colombia
"""

from sklearn.linear_model import LinearRegression
import pandas as pd
from joblib import dump
import os

# Leer los datos procesados
df = pd.read_csv("/opt/airflow/salidas/datos_procesados.csv")

# Convertir la fecha a formato numérico para regresión
df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')
df = df.dropna(subset=["fecha"])
df["fecha"] = df["fecha"].view("int64") // 10**9  # convertir a segundos UNIX

# Variables predictoras y objetivo
X = df[["fecha"]]
y = df["valor"]

# Entrenar el modelo
modelo = LinearRegression().fit(X, y)

# Hacer predicciones
predicciones = modelo.predict(X)

# Crear carpeta de salida (si no existe)
os.makedirs("/opt/airflow/salidas", exist_ok=True)

# Guardar las predicciones en archivo CSV
pd.DataFrame(predicciones, columns=["prediccion"]).to_csv("/opt/airflow/salidas/predicciones_ml.csv", index=False)

# Guardar el modelo entrenado como archivo .pkl (con joblib)
dump(modelo, "/opt/airflow/salidas/modelo_entrenado.pkl")

print("✅ Modelo entrenado y predicciones guardadas en /opt/airflow/salidas/")
