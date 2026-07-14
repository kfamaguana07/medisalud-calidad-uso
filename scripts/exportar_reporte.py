import json
import os
import numpy as np
from metricas_iso25022 import generar_reporte

def convertir(obj):
    if isinstance(obj, dict):
        return {k: convertir(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convertir(v) for v in obj]
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.bool_):
        return bool(obj)
    return obj

reporte, eficiencia_sede = generar_reporte()

salida = {
    "metricas": convertir(reporte),
    "eficiencia_por_sede": eficiencia_sede.to_dict(orient="records"),
}

os.makedirs("dashboards", exist_ok=True)
with open("dashboards/indicadores.json", "w", encoding="utf-8") as f:
    json.dump(salida, f, indent=2, ensure_ascii=False)

print("Reporte exportado a dashboards/indicadores.json")
