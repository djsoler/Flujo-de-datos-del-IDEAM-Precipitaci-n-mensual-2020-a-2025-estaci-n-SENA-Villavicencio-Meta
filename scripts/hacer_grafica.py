import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("salidas/datos_procesados.csv")

df.plot(x='fecha', y='valor', kind='line')
plt.title("Gráfico de valores procesados")
plt.xlabel("Fecha")
plt.ylabel("Valor")
plt.grid(True)

os.makedirs("salidas", exist_ok=True)
plt.savefig("salidas/resultado.png")
print("✅ Gráfica guardada en 'salidas/resultado.png'")
