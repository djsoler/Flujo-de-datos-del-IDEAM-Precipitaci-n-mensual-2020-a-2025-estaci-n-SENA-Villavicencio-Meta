from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import dask.dataframe as dd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import os

# Rutas
path = "/opt/airflow/salidas/"
db_url = 'postgresql://airflow:airflow@postgres:5432/airflow'

# Argumentos por defecto
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 1. Ingesta de datos (Kafka simulado)
def leer_datos_kafka():
    input_path = '/opt/airflow/salidas/datos_procesados.csv'
    output_path = '/opt/airflow/salidas/datos_leidos.csv'

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Archivo no encontrado: {input_path}")

    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)
    print(f'Datos simulados como Kafka leídos desde {input_path} y guardados en {output_path}')

# 2. Procesamiento con Dask
def procesar_datos_dask():
    df = dd.read_csv(f'{path}datos_leidos.csv')
    df['valor'] = df['valor'] * 2
    df.compute().to_csv(f'{path}datos_procesados.csv', index=False)

# 3. Guardar en SQL
def guardar_en_sql():
    df = pd.read_csv(f'{path}datos_procesados.csv')
    engine = create_engine(db_url)
    df.to_sql('tabla_datos', engine, if_exists='replace', index=False)

# 4a. Gráfico de línea
def graficar_linea():
    df = pd.read_csv(f'{path}datos_procesados.csv')
    plt.figure()
    plt.plot(df['valor'])
    plt.title('Gráfico de Línea - Valor')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.savefig(f'{path}grafico_linea.png')

# 4b. Función para graficar outliers
def crear_grafico_outliers():
    os.system("python /opt/airflow/scripts/graficar_outliers.py")

# 4c. Histograma
def graficar_histograma():
    df = pd.read_csv(f'{path}datos_procesados.csv')
    plt.figure()
    df['valor'].hist()
    plt.title('Histograma de valores')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.savefig(f'{path}grafico_histograma.png')

# 5. Modelo simple en línea (visual)
def modelo_ml():
    df = pd.read_csv(f'{path}datos_procesados.csv')
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['valor'].values
    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)
    plt.figure()
    plt.scatter(X, y, label='Datos reales')
    plt.plot(X, y_pred, color='red', label='Predicción')
    plt.title('Regresión lineal')
    plt.legend()
    plt.savefig(f'{path}modelo_ml.png')

# 6. Ejecutar script externo para entrenar modelo
def entrenar_modelo_ml():
    script_path = "/opt/airflow/scripts/modelo_ml.py"
    os.system(f"python {script_path}")

# 7. Predicción a futuro de precipitaciones
def predecir_futuro():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression

    df = pd.read_csv(f'{path}datos_procesados.csv')

    # Índice como variable temporal
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['valor'].values

    # Entrenar modelo de regresión lineal
    model = LinearRegression().fit(X, y)

    # Crear nuevos índices para los próximos 6 meses
    meses_futuros = 6
    X_future = np.arange(len(df), len(df) + meses_futuros).reshape(-1, 1)
    y_pred_future = model.predict(X_future)

    # Guardar predicciones en un CSV
    df_futuro = pd.DataFrame({
        'mes': np.arange(1, meses_futuros + 1),
        'prediccion_precipitacion': y_pred_future
    })
    df_futuro.to_csv(f'{path}predicciones_futuras.csv', index=False)

    # Graficar predicción
    plt.figure()
    plt.plot(X, y, label='Histórico')
    plt.plot(X_future, y_pred_future, '--o', color='green', label='Futuro')
    plt.title('Predicción de Precipitaciones - Próximos 6 Meses')
    plt.xlabel('Mes (índice)')
    plt.ylabel('Precipitación (mm)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{path}grafico_prediccion_futura.png')
    print(f" Predicciones y gráfico guardados en {path}")

# DAG
with DAG(
    dag_id='proyecto_bigdata',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['bigdata'],
    description='Flujo de datos del IDEAM - Precipitación mensual 2020-2025. Departamento del Meta, estación SENA (Villavicencio).',
) as dag:

    t1 = PythonOperator(task_id='leer_kafka', python_callable=leer_datos_kafka)
    t2 = PythonOperator(task_id='procesar_datos_dask', python_callable=procesar_datos_dask)
    t3 = PythonOperator(task_id='guardar_postgresql', python_callable=guardar_en_sql)
    t4a = PythonOperator(task_id='crear_grafico_linea', python_callable=graficar_linea)
    t4b = PythonOperator(task_id='crear_grafico_outliers', python_callable=crear_grafico_outliers)
    t4c = PythonOperator(task_id='crear_histograma', python_callable=graficar_histograma)
    t5 = PythonOperator(task_id='modelo_machine_learning', python_callable=modelo_ml)
    t6 = PythonOperator(task_id='entrenar_modelo_ml', python_callable=entrenar_modelo_ml)
    t7 = PythonOperator(task_id='prediccion_futuro', python_callable=predecir_futuro)

    # Dependencias
    t1 >> t2 >> t3 >> [t4a, t4b, t4c] >> t5 >> t6 >> t7