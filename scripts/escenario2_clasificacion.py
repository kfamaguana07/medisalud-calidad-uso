import csv
import os

# Detecta automáticamente la raíz del proyecto para evitar errores de ruta
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta_csv = os.path.join(base_dir, 'data', 'incidentes_2025_iso_25022.csv')

# Los IDs exactos que pide la guía del taller (Tabla 2.2 y fragmento de la página 20)
ids_solicitados = ['1001', '1002', '1003', '1004', '1005', '1006']

try:
    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        
        # Leer y mostrar encabezados
        encabezado = next(lector_csv)
        print("Encabezados:", encabezado)
        print("-" * 50)
        
        registros_encontrados = []
        
        for registro in lector_csv:
            id_incidente = registro[0] # El ID está en la primera columna
            if id_incidente in ids_solicitados:
                registros_encontrados.append(registro)
                print(f"Registro encontrado (ID {id_incidente}): {registro}")
        
        print("-" * 50)
        print(f"Se encontraron {len(registros_encontrados)} de {len(ids_solicitados)} incidentes solicitados.")
                
except FileNotFoundError:
    print(f"No se encontró el archivo en: {ruta_csv}")