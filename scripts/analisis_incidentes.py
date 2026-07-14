"""
Analisis del dataset de incidentes 2025 - MediSalud HIS
Escenario 3 - ISO/IEC 25022 / SQuaRE
---------------------------------------------------------
Requiere: pandas, matplotlib
Instalacion: pip install pandas matplotlib --break-system-packages
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # backend sin interfaz grafica, para guardar a archivo
import matplotlib.pyplot as plt

CSV_PATH = 'data/incidentes_2025_iso_25022.csv'

# ============================================================
# 1. CARGA DEL DATASET
# ============================================================
df = pd.read_csv(CSV_PATH)
print("Total registros:", len(df))
print(df.head())

# ============================================================
# 2. CONTEOS POR CATEGORIA
# ============================================================
print("\n--- Incidentes por modulo ---")
conteo_modulo = df['modulo'].value_counts()
print(conteo_modulo)

print("\n--- Incidentes por rol_usuario ---")
conteo_rol = df['rol_usuario'].value_counts()
print(conteo_rol)

print("\n--- Incidentes por sede ---")
conteo_sede = df['sede'].value_counts()
print(conteo_sede)

# Top descripciones repetidas dentro de un modulo especifico (ej. HCE)
print("\n--- Top descripciones mas frecuentes en modulo HCE ---")
top_hce = df[df.modulo == 'HCE']['descripcion'].value_counts().head(8)
print(top_hce)

print("\n--- Top descripciones mas frecuentes en Portal Citas ---")
top_portal = df[df.modulo == 'Portal Citas']['descripcion'].value_counts().head(8)
print(top_portal)

# ============================================================
# 3. EXTRACCION DE TIEMPOS MENCIONADOS EN TEXTO LIBRE (REGEX)
# ============================================================
# Caso A: "Nota de evolucion tarda Xs en guardarse"
nota = df[df['descripcion'].str.contains('Nota de evolucion tarda', na=False)]
nota_tiempos = nota['descripcion'].str.extract(r'tarda (\d+)s').astype(float)

print("\n--- Nota de evolucion: tiempos reportados (segundos) ---")
print("n =", len(nota))
print("promedio =", nota_tiempos.mean()[0])
print("maximo   =", nota_tiempos.max()[0])

# Caso B: "Tiempo de carga de la ficha clinica supera los Xs"
ficha = df[df['descripcion'].str.contains('Tiempo de carga de la ficha clinica', na=False)]
ficha_tiempos = ficha['descripcion'].str.extract(r'supera los (\d+)s').astype(float)

print("\n--- Carga de ficha clinica: tiempos reportados (segundos) ---")
print("n =", len(ficha))
print("promedio =", ficha_tiempos.mean()[0])
print("maximo   =", ficha_tiempos.max()[0])

# ============================================================
# 4. CONTRASTE CON EL REQUERIMIENTO RNF-01 (umbral = 8 segundos)
# ============================================================
UMBRAL_RNF01 = 8
pct_incumple = (nota_tiempos[0] > UMBRAL_RNF01).mean() * 100
print(f"\n% de incidentes de 'nota de evolucion' que incumplen "
      f"RNF-01 (>{UMBRAL_RNF01}s): {pct_incumple:.1f}%")

# ============================================================
# 5. GRAFICOS
# ============================================================
plt.rcParams['font.family'] = 'DejaVu Sans'

# --- Grafico 1: incidentes por modulo (barras horizontales) ---
counts_modulo = conteo_modulo.sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(7, 4.2))
bars = ax.barh(counts_modulo.index, counts_modulo.values, color='#2E6E9E')
ax.set_xlabel('Numero de incidentes reportados (2025)')
ax.set_title('Distribucion de incidentes por modulo - MediSalud HIS', fontsize=11)
for bar, val in zip(bars, counts_modulo.values):
    ax.text(val + 5, bar.get_y() + bar.get_height() / 2, str(val),
            va='center', fontsize=9)
plt.tight_layout()
plt.savefig('incidentes_por_modulo.png', dpi=200)
plt.close(fig)

# --- Grafico 2: incidentes por sede (barras verticales) ---
counts_sede = conteo_sede
colores = ['#2E6E9E', '#4E8FB8', '#7FB3D5', '#A9CCE3', '#D4E6F1']
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(counts_sede.index, counts_sede.values, color=colores[:len(counts_sede)])
ax.set_ylabel('Numero de incidentes')
ax.set_title('Incidentes reportados por sede - MediSalud HIS (2025)', fontsize=11)
for i, val in enumerate(counts_sede.values):
    ax.text(i, val + 8, str(val), ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('incidentes_por_sede.png', dpi=200)
plt.close(fig)

print("\nGraficos guardados: incidentes_por_modulo.png, incidentes_por_sede.png")
