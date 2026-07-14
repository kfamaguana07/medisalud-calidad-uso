import json
from metricas_iso25022 import generar_reporte
import os

reporte, eficiencia_sede = generar_reporte()

salida = {
    "metricas": reporte,
    "eficiencia_por_sede": eficiencia_sede.to_dict(orient="records"),
}

os.makedirs("dashboards", exist_ok=True)
with open("dashboards/indicadores.json", "w", encoding="utf-8") as f:
    json.dump(salida, f, indent=2, ensure_ascii=False, default=str)

print("Reporte exportado a dashboards/indicadores.json")
