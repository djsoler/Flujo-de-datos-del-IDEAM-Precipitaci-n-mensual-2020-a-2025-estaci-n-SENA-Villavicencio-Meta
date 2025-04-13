# Esquema del Data Warehouse - Proyecto Big Data

## Justificación como Data Warehouse
### Datos históricos: IDEAM (2020–2025)

### Diferentes etapas del pipeline: crudo → limpio → predicción

### Posibilidad de análisis por tiempo y proyecciones

### Preparado para consultas complejas

## Tablas utilizadas

### 1. datos_leidos
- `fecha`: DATE
- `estacion`: VARCHAR(100)
- `precipitacion_mm`: FLOAT  
> Datos crudos originales obtenidos del IDEAM.

### 2. datos_procesados
- `fecha`: DATE
- `precipitacion_mm`: FLOAT  
> Datos limpios y transformados con Dask.

### 3. predicciones
- `fecha`: DATE
- `precipitacion_predicha_mm`: FLOAT  
> Resultados del modelo de Machine Learning.

---

## Consultas complejas posibles

Este pequeño Data Warehouse permite hacer consultas como:

```sql
SELECT AVG(precipitacion_mm)
FROM datos_procesados
WHERE fecha BETWEEN '2022-01-01' AND '2022-12-31';
