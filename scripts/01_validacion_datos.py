import pandas as pd

df = pd.read_csv("data/logs_hce.csv")

# 1. Verificar valores nulos
print("Valores nulos por columna:")
print(df.isnull().sum())

# 2. Verificar rangos logicos
print("\nTiempos fuera de rango (negativos o mayores a 120s):")
print(df[(df["tiempo_segundos"] < 0) | (df["tiempo_segundos"] > 120)])

# 3. Verificar duplicados
print("\nEventos duplicados:", df.duplicated(subset=["evento_id"]).sum())

# 4. Resumen descriptivo
print("\nResumen estadistico de tiempo_segundos:")
print(df["tiempo_segundos"].describe())
