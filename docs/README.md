# Proyecto Final Big Data - Airflow + Kafka + Dask + SQL + ML

Este proyecto demuestra un flujo de procesamiento de datos usando herramientas de Big Data. Está orquestado con **Apache Airflow**, y combina **Kafka, Dask, PostgreSQL/MySQL, Matplotlib y Scikit-learn**.


# 📁 Estructura del Proyecto

```
airflow/
│
├── dags/
│   ├── proyecto_bigdata_dag.py       # Archivo principal del DAG que orquesta el flujo
│   ├── _pycache_                     # Guarda versiones compiladas de los scripts
├── logs/
│   ├── dag_id=proyecto_bigdata       # Logs del DAG ejecutado
│   ├── dag_processor_manager         # Logs de Airflow
│   ├── scheduler                     # Logs del programador de tareas
├── docs/                            
│   ├── README                        # Este archivo, que describe que contiene el proyecto y que hace cada cosa
│   ├── Reseña                        # Reseña de flujo de procesamiento de datos
│   ├── Taller final de Big Data
│   ├── Notas
├── scripts/                          # Carpeta auxiliar
│   ├── guardar_en_sql.py             # Carga y guarda los datos transformados en SQL
│   ├── hacer_grafica.py              # Crea una gráfica desde los datos
│   ├── kafka_ingest.py               # Simula la ingesta de datos con Kafka
│   ├── modelo_ml.py                  # Entrena un modelo de machine learning
│   ├── transformar_datos.py          # Prcoesa, limpiando y transformando los datos
│    salidas/ 
│   ├── datos_leidos.csv
│   ├── datos_procesados.csv
│   ├── predicciones.csv
│   ├── predicciones_futuras.csv
│   ├── predicciones_ml.csv
│   ├── grafico.png
│   ├── grafico_histograma.png
│   ├── grafico_histograma.png
│   ├── grafico_histograma.png
│   ├── grafico_prediccion_futura.png
│   ├── modelo_ml.png
│   ├── modelo_entrenado.pkl 
│   docker-compose.yml
│   .env
│   descargaDhime.csv
│   docker-compose.yml
│   Dockerfile
│   schema
```
---

# ¿Qué hace cada script?

- `kafka_ingest.py`: Simula la ingesta de datos desde Kafka (puede leer un archivo CSV o generar datos).
- `transformar_datos.py`: Realiza limpieza, filtrado o transformación de los datos crudos.
- `guardar_en_sql.py`: Inserta los datos en una base de datos SQL (como MySQL o PostgreSQL).
- `hacer_grafica.py`: Genera una gráfica (PNG) para visualizar los datos procesados.
- `modelo_ml.py`: Entrena un modelo de machine learning (regresión o clasificación).
- `airflowdagsproyecto_bigdata_dag.py`: Ejemplo de prueba inicial del DAG.
---

# Cómo ejecutar Airflow

1. Abrir terminal como windows PowerShell y activa entorno virtual.
2. Iniciar la base de datos de Airflow:

```bash
airflow db init
```
3. Creación de un usuario administrador:

```bash
airflow users create \
  --username admin \
  --firstname Johanna \
  --lastname Soler \
  --role Admin \
  --email johannasolermine@gmail.com
```
4. Iniciar los servicios de Airflow:

```bash
airflow scheduler
# En otra terminal:
airflow webserver
```
5. Abrir el navegador y visitar: [http://localhost:8080](http://localhost:8080)
---
# ¿Qué hace cada tarea del DAG?

El archivo `proyecto_bigdata_dag.py` contiene un DAG con las siguientes tareas:

| Task ID                   | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `leer_kafka`              | Simula la ingesta de datos desde archivo CSV (como si viniera de Kafka).   |
| `procesar_datos_dask`     | Usa Dask para procesar los datos leídos.                                   |
| `guardar_postgresql`      | Guarda los datos transformados en PostgreSQL.                              |
| `crear_grafico_linea`     | Genera gráfico de línea con Matplotlib.                                    |
| `crear_grafico_outliers`  | Detección visual de valores extremos.                                      |
| `crear_histograma`        | Histograma de frecuencias para la variable.                                |
| `modelo_machine_learning` | Entrena modelo de regresión lineal.                                        |
| `entrenar_modelo_ml`      | Script separado para guardar modelo (`pkl`) y predicciones.                |
| `prediccion_futuro`       | Predice valores futuros y genera gráfica y CSV de resultados.              |

---

# Requisitos

- Docker
- Python 3.10
- Apache Airflow 2.8.1
- Kafka
- Dask
- pandas, matplotlib, scikit-learn
- PostgreSQL

---

# Resultado esperado

Al ejecutar el DAG desde la interfaz de Airflow:

1. Se ingesta, procesa y guarda un dataset simulado de precipitaciones
2. Se visualiza mediante tres tipos de gráficas
3. Se entrena un modelo de ML
4. Se hacen predicciones sobre los próximos meses
5. Se guardan los resultados en .csv y .png

---