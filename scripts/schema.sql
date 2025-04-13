-- Tabla con los datos leídos desde el CSV original
CREATE TABLE datos_leidos (
    fecha DATE,
    estacion VARCHAR(100),
    precipitacion_mm FLOAT
);

-- Tabla con los datos ya procesados (puede incluir valores transformados, limpios, etc.)
CREATE TABLE datos_procesados (
    fecha DATE,
    precipitacion_mm FLOAT
);

-- Tabla de predicciones (por ejemplo, generadas por un modelo de ML)
CREATE TABLE predicciones (
    fecha DATE,
    precipitacion_predicha_mm FLOAT
);

