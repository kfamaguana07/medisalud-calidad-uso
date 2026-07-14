"""
Genera un log sintetico de respuestas de encuestas de satisfaccion CSAT.
"""
import csv
import random

random.seed(42)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
ROLES = ["Medico", "Paciente", "Personal de admision", "Enfermeria"]

filas = []
for i in range(1, 151):
    sede = random.choice(SEDES)
    rol = random.choice(ROLES)
    # Sesgo: medicos suelen dar menor puntaje por la lentitud, pacientes varian.
    if rol == "Medico":
        puntaje = random.choice([1, 2, 2, 3, 4])
    else:
        puntaje = random.choice([3, 4, 4, 5, 5])
        
    comentario = ""
    if puntaje <= 2:
        comentario = "Sistema muy lento."
    elif puntaje == 5:
        comentario = "Excelente servicio."
        
    filas.append({
        "respuesta_id": i,
        "sede": sede,
        "rol": rol,
        "puntaje_csat": puntaje,
        "comentario": comentario
    })

with open("data/encuesta_satisfaccion.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filas[0].keys())
    writer.writeheader()
    writer.writerows(filas)

print(f"Se generaron {len(filas)} encuestas en data/encuesta_satisfaccion.csv")
