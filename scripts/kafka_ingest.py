import time
import random
import csv
from datetime import datetime
import os

def simular_ingesta():
    # Asegura que exista la carpeta 'data'
    os.makedirs("C:/Users/JONANNA/Desktop/airflow/data", exist_ok=True)

    archivo_salida = "C:/Users/JONANNA/Desktop/airflow/data/datos.csv"  # nombre esperado por otros scripts
    
    with open(archivo_salida, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["fecha", "valor"])  # ← importante: nombre de columnas correctos

        for _ in range(10):
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            valor = round(random.uniform(10.0, 100.0), 2)
            escritor.writerow([fecha, valor])
            print(f"Ingresado: {fecha} - {valor}")
            time.sleep(1)

if __name__ == "__main__":
    simular_ingesta()
