# graficar_outliers.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta de los archivos
path = "/opt/airflow/salidas/"
file = os.path.join(path, "datos_procesados.csv")  # o usar "datos_leidos.csv"

# Leer los datos
df = pd.read_csv(file)
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')

# Identificar outliers usando el criterio del rango intercuartílico (IQR)
Q1 = df['valor'].quantile(0.25)
Q3 = df['valor'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['valor'] < Q1 - 1.5 * IQR) | (df['valor'] > Q3 + 1.5 * IQR)]

# Graficar serie + outliers resaltados
plt.figure(figsize=(12, 6))
plt.plot(df['fecha'], df['valor'], label='Precipitación mensual', color='blue', alpha=0.7)
plt.scatter(outliers['fecha'], outliers['valor'], color='red', label='Outliers', zorder=5)
plt.title("Serie de Precipitación con Detección de Outliers\nVillavicencio, Estación SENA (2020-2025)")
plt.xlabel("Fecha")
plt.ylabel("Valor (mm)")
plt.legend()
plt.grid(True)

# Fuente en el pie de gráfico
plt.figtext(0.99, 0.01,
            "Fuente: IDEAM. Datos de precipitación mensual total del 2020 al 2025 - Villavicencio, estación SENA.",
            horizontalalignment='right',
            fontsize=8)

# Guardar el gráfico
plt.tight_layout()
plt.savefig(os.path.join(path, "grafico_outliers.png"))
print(" Gráfico de outliers generado y guardado.")
