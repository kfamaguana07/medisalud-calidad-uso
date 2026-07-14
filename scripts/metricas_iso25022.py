"""
Modulo de calculo de metricas de Calidad en Uso (ISO/IEC 25022)
para el sistema MediSalud HIS.

Cada funcion retorna un diccionario con: valor, unidad, umbral y estado.
"""
import pandas as pd

UMBRAL_TIEMPO_TAREA = 8.0 # segundos, segun RNF-01
UMBRAL_TASA_ERROR_FACT = 0.01 # 1%, segun RNF-03
UMBRAL_EFECTIVIDAD = 0.95 # 95% de completitud esperada

def cargar_datos():
    """Carga los tres datasets base del programa de medicion."""
    logs = pd.read_csv("data/logs_hce.csv")
    encuesta = pd.read_csv("data/encuesta_satisfaccion.csv")
    incidentes = pd.read_csv("data/incidentes_2025_iso_25022.csv")
    return logs, encuesta, incidentes

def metrica_efectividad(logs: pd.DataFrame) -> dict:
    """
    Efectividad = notas completadas correctamente / notas intentadas.
    """
    total = len(logs)
    completadas = logs["completada"].sum()
    valor = round(completadas / total, 4) if total else 0.0
    return {
        "nombre": "Completitud de registro de HCE",
        "caracteristica": "Efectividad",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_EFECTIVIDAD,
        "cumple": valor >= UMBRAL_EFECTIVIDAD,
    }

def metrica_eficiencia(logs: pd.DataFrame) -> dict:
    """
    Eficiencia = tiempo promedio de registro de nota clinica (segundos).
    """
    valor = round(logs["tiempo_segundos"].mean(), 2)
    return {
        "nombre": "Tiempo promedio de registro de HCE",
        "caracteristica": "Eficiencia",
        "valor": valor,
        "unidad": "segundos",
        "umbral": UMBRAL_TIEMPO_TAREA,
        "cumple": valor <= UMBRAL_TIEMPO_TAREA,
    }

def metrica_eficiencia_por_sede(logs: pd.DataFrame) -> pd.DataFrame:
    """Desagrega el tiempo promedio de tarea por sede (Cobertura de Contexto)."""
    return (
        logs.groupby("sede")["tiempo_segundos"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"tiempo_segundos": "tiempo_promedio_segundos"})
    )

def metrica_satisfaccion(encuesta: pd.DataFrame) -> dict:
    """
    Satisfaccion = promedio de puntaje CSAT (escala 1-5), normalizado a 0-1.
    """
    promedio_csat = encuesta["puntaje_csat"].mean()
    valor = round(promedio_csat / 5, 4)
    return {
        "nombre": "Indice de satisfaccion (CSAT normalizado)",
        "caracteristica": "Satisfaccion",
        "valor": valor,
        "unidad": "proporcion (0-1)",
        "umbral": 0.80,
        "cumple": valor >= 0.80,
    }

def metrica_libertad_riesgo(incidentes: pd.DataFrame, total_transacciones: int) -> dict:
    """
    Libertad de Riesgo = tasa de incidentes de facturacion sobre el total
    de transacciones de facturacion procesadas en el periodo.
    """
    incidentes_facturacion = incidentes[incidentes["modulo"] == "Facturacion"]
    valor = round(len(incidentes_facturacion) / total_transacciones, 4)
    return {
        "nombre": "Tasa de errores de facturacion",
        "caracteristica": "Libertad de Riesgo",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_TASA_ERROR_FACT,
        "cumple": valor <= UMBRAL_TASA_ERROR_FACT,
    }

def generar_reporte():
    """Orquesta el calculo de todas las metricas y consolida el resultado."""
    logs, encuesta, incidentes = cargar_datos()
    
    reporte = {
        "efectividad": metrica_efectividad(logs),
        "eficiencia": metrica_eficiencia(logs),
        "satisfaccion": metrica_satisfaccion(encuesta),
        # Se asume un total simulado de 8500 transacciones de facturacion
        # en el periodo de medicion (dato provisto por el area financiera).
        "libertad_riesgo": metrica_libertad_riesgo(incidentes, total_transacciones=8500),
    }
    
    eficiencia_sede = metrica_eficiencia_por_sede(logs)
    
    return reporte, eficiencia_sede

if __name__ == "__main__":
    reporte, eficiencia_sede = generar_reporte()
    print("=== Reporte de Calidad en Uso - MediSalud HIS ===\n")
    for clave, metrica in reporte.items():
        estado = "CUMPLE" if metrica["cumple"] else "NO CUMPLE"
        print(f"{metrica['nombre']}: {metrica['valor']} {metrica['unidad']} "
              f"(umbral: {metrica['umbral']}) -> {estado}")
    
    print("\n=== Eficiencia por sede (Cobertura de Contexto) ===")
    print(eficiencia_sede.to_string(index=False))
