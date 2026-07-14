"""
Generador de evidencia grafica y datos para los Escenarios 4 al 12.
Genera todos los graficos PNG y datos necesarios para los informes LaTeX.
Requiere: pandas, matplotlib
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import re
import json

# ============================================================
# CONFIGURACION
# ============================================================
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
REPORTES_DIR = os.path.join(os.path.dirname(__file__), '..', 'reportes')
SCRIPTS_DIR = os.path.dirname(__file__)

os.makedirs(REPORTES_DIR, exist_ok=True)
os.makedirs(os.path.join(REPORTES_DIR, 'img'), exist_ok=True)
IMG_DIR = os.path.join(REPORTES_DIR, 'img')

plt.rcParams['font.family'] = 'DejaVu Sans'
COLORES = ['#1B4F72', '#2E6E9E', '#4E8FB8', '#7FB3D5', '#A9CCE3', '#D4E6F1', '#EBF5FB']

# ============================================================
# CARGA DE DATOS
# ============================================================
logs = pd.read_csv(os.path.join(DATA_DIR, 'logs_hce.csv'))
encuesta = pd.read_csv(os.path.join(DATA_DIR, 'encuesta_satisfaccion.csv'))
incidentes = pd.read_csv(os.path.join(DATA_DIR, 'incidentes_2025_iso_25022.csv'))

print(f"Logs HCE: {len(logs)} registros")
print(f"Encuestas CSAT: {len(encuesta)} registros")
print(f"Incidentes: {len(incidentes)} registros")

# ============================================================
# ESCENARIO 5: Grafico de priorizacion de tareas
# ============================================================
tareas = ['Registro HCE', 'Agendar cita', 'Facturar consulta',
          'Teleconsulta', 'Adm. medicamentos', 'Historial lab.']
impacto = [5, 5, 5, 3, 5, 2]
frecuencia = [5, 5, 3, 3, 3, 5]
prioridad_calc = [i*f for i, f in zip(impacto, frecuencia)]

fig, ax = plt.subplots(figsize=(8, 5))
colors_bar = ['#1B4F72' if p >= 20 else '#4E8FB8' if p >= 9 else '#A9CCE3' for p in prioridad_calc]
bars = ax.barh(tareas, prioridad_calc, color=colors_bar, edgecolor='#1B4F72', linewidth=0.5)
ax.set_xlabel('Puntuacion de priorizacion (Impacto x Frecuencia)', fontsize=10)
ax.set_title('Priorizacion de tareas para medicion ISO/IEC 25022\nMediSalud HIS', fontsize=11)
for bar, val in zip(bars, prioridad_calc):
    ax.text(val + 0.3, bar.get_y() + bar.get_height()/2, str(val),
            va='center', fontsize=9, fontweight='bold')
ax.axvline(x=15, color='red', linestyle='--', linewidth=0.8, label='Umbral prioridad alta')
ax.legend(loc='lower right', fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'priorizacion_tareas.png'), dpi=200)
plt.close(fig)
print("[OK] priorizacion_tareas.png")

# ============================================================
# ESCENARIO 7: Validacion de datos y graficos exploratorios
# ============================================================
# Distribucion de tiempos de tarea
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# Histograma general
axes[0].hist(logs['tiempo_segundos'], bins=40, color='#2E6E9E', edgecolor='white', linewidth=0.3)
axes[0].axvline(x=8.0, color='red', linestyle='--', linewidth=1.5, label='Umbral RNF-01 (8s)')
axes[0].set_xlabel('Tiempo de registro (segundos)')
axes[0].set_ylabel('Frecuencia')
axes[0].set_title('Distribucion de tiempos de registro HCE\n(n={:,})'.format(len(logs)))
axes[0].legend(fontsize=8)

# Boxplot por sede
sedes_order = logs.groupby('sede')['tiempo_segundos'].median().sort_values(ascending=False).index
data_boxplot = [logs[logs['sede'] == s]['tiempo_segundos'].values for s in sedes_order]
bp = axes[1].boxplot(data_boxplot, tick_labels=list(sedes_order), patch_artist=True)
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(COLORES[i % len(COLORES)])
axes[1].axhline(y=8.0, color='red', linestyle='--', linewidth=1.5, label='Umbral RNF-01 (8s)')
axes[1].set_ylabel('Tiempo de registro (segundos)')
axes[1].set_title('Tiempo de registro HCE por sede')
axes[1].legend(fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'distribucion_tiempos_hce.png'), dpi=200)
plt.close(fig)
print("[OK] distribucion_tiempos_hce.png")

# Completitud (Efectividad) por sede
efect_sede = logs.groupby('sede')['completada'].mean().reset_index()
efect_sede.columns = ['sede', 'tasa_completitud']
efect_sede = efect_sede.sort_values('tasa_completitud', ascending=True)

fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.barh(efect_sede['sede'], efect_sede['tasa_completitud'] * 100,
               color='#2E6E9E', edgecolor='#1B4F72', linewidth=0.5)
ax.axvline(x=95, color='red', linestyle='--', linewidth=1.5, label='Umbral (95%)')
ax.set_xlabel('Tasa de completitud (%)')
ax.set_title('Efectividad: completitud de registro HCE por sede')
for bar, val in zip(bars, efect_sede['tasa_completitud'] * 100):
    ax.text(val + 0.2, bar.get_y() + bar.get_height()/2, f'{val:.1f}%',
            va='center', fontsize=9)
ax.legend(fontsize=8)
ax.set_xlim(90, 100)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'efectividad_por_sede.png'), dpi=200)
plt.close(fig)
print("[OK] efectividad_por_sede.png")

# ============================================================
# ESCENARIO 7: Encuesta CSAT
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# Distribucion de puntajes CSAT
conteo_csat = encuesta['puntaje_csat'].value_counts().sort_index()
axes[0].bar(conteo_csat.index, conteo_csat.values, color=COLORES[:5], edgecolor='#1B4F72', linewidth=0.5)
axes[0].set_xlabel('Puntaje CSAT (1-5)')
axes[0].set_ylabel('Numero de respuestas')
axes[0].set_title('Distribucion de puntajes CSAT\n(n={})'.format(len(encuesta)))
axes[0].set_xticks([1, 2, 3, 4, 5])

# CSAT por rol
csat_rol = encuesta.groupby('rol')['puntaje_csat'].mean().sort_values()
bars = axes[1].barh(csat_rol.index, csat_rol.values, color='#2E6E9E', edgecolor='#1B4F72', linewidth=0.5)
axes[1].axvline(x=4.0, color='red', linestyle='--', linewidth=1.5, label='Umbral (4.0/5)')
axes[1].set_xlabel('Puntaje CSAT promedio')
axes[1].set_title('Satisfaccion promedio por rol de usuario')
for bar, val in zip(bars, csat_rol.values):
    axes[1].text(val + 0.03, bar.get_y() + bar.get_height()/2, f'{val:.2f}',
            va='center', fontsize=9)
axes[1].legend(fontsize=8)
axes[1].set_xlim(0, 5.5)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'encuesta_csat.png'), dpi=200)
plt.close(fig)
print("[OK] encuesta_csat.png")

# ============================================================
# ESCENARIO 8: Resultados de metricas automatizadas
# ============================================================
# Calculo de metricas
total_logs = len(logs)
completadas = logs['completada'].sum()
efectividad = completadas / total_logs
eficiencia = logs['tiempo_segundos'].mean()
csat_norm = encuesta['puntaje_csat'].mean() / 5
inc_fact = len(incidentes[incidentes['modulo'] == 'Facturacion'])
libertad_riesgo = inc_fact / 8500  # total transacciones estimadas

efic_sede = logs.groupby('sede')['tiempo_segundos'].mean()
max_sede = efic_sede.max()
min_sede = efic_sede.min()
cobertura = 1 - abs(max_sede - min_sede) / max_sede

metricas = {
    'Efectividad': {'valor': round(efectividad, 4), 'umbral': 0.95,
                    'cumple': efectividad >= 0.95, 'unidad': 'proporcion'},
    'Eficiencia': {'valor': round(eficiencia, 2), 'umbral': 8.0,
                   'cumple': eficiencia <= 8.0, 'unidad': 'segundos'},
    'Satisfaccion': {'valor': round(csat_norm, 4), 'umbral': 0.80,
                     'cumple': csat_norm >= 0.80, 'unidad': 'proporcion'},
    'Libertad de Riesgo': {'valor': round(libertad_riesgo, 4), 'umbral': 0.01,
                           'cumple': libertad_riesgo <= 0.01, 'unidad': 'proporcion'},
    'Cobertura de Contexto': {'valor': round(cobertura, 4), 'umbral': 0.90,
                              'cumple': cobertura >= 0.90, 'unidad': 'proporcion'}
}

# Dashboard de metricas
fig, ax = plt.subplots(figsize=(10, 4))
nombres = list(metricas.keys())
valores = [m['valor'] for m in metricas.values()]
umbrales = [m['umbral'] for m in metricas.values()]
cumple = [m['cumple'] for m in metricas.values()]

# Normalizar para visualizacion (eficiencia se invierte: menor es mejor)
vals_norm = []
umbs_norm = []
for n, v, u in zip(nombres, valores, umbrales):
    if n == 'Eficiencia':
        vals_norm.append(min(1.0, u / v) if v > 0 else 1.0)
        umbs_norm.append(1.0)
    elif n == 'Libertad de Riesgo':
        vals_norm.append(max(0, 1 - v/0.1))
        umbs_norm.append(max(0, 1 - u/0.1))
    else:
        vals_norm.append(v)
        umbs_norm.append(u)

colores_met = ['#27AE60' if c else '#E74C3C' for c in cumple]
bars = ax.barh(nombres, vals_norm, color=colores_met, edgecolor='white', linewidth=1.5, height=0.6)
for i, (bar, v, u_orig, c) in enumerate(zip(bars, valores, umbrales, cumple)):
    estado = 'CUMPLE' if c else 'NO CUMPLE'
    unidad = metricas[nombres[i]]['unidad']
    txt = f'{v} {unidad}  (umbral: {u_orig})  [{estado}]'
    ax.text(0.02, bar.get_y() + bar.get_height()/2, txt,
            va='center', fontsize=8.5, fontweight='bold', color='white')

ax.set_xlim(0, 1.1)
ax.set_title('Dashboard de Metricas ISO/IEC 25022 - MediSalud HIS', fontsize=12, fontweight='bold')
ax.set_xlabel('Cumplimiento normalizado (1.0 = objetivo)')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'dashboard_metricas.png'), dpi=200)
plt.close(fig)
print("[OK] dashboard_metricas.png")

# Eficiencia por sede (grafico de barras)
efic_sede_df = efic_sede.sort_values(ascending=True).reset_index()
efic_sede_df.columns = ['sede', 'tiempo_promedio']

fig, ax = plt.subplots(figsize=(7, 4))
colors_sede = ['#E74C3C' if t > 8.0 else '#27AE60' for t in efic_sede_df['tiempo_promedio']]
bars = ax.barh(efic_sede_df['sede'], efic_sede_df['tiempo_promedio'],
               color=colors_sede, edgecolor='#1B4F72', linewidth=0.5)
ax.axvline(x=8.0, color='red', linestyle='--', linewidth=1.5, label='Umbral RNF-01 (8s)')
ax.set_xlabel('Tiempo promedio de registro (segundos)')
ax.set_title('Eficiencia de registro HCE por sede\n(Cobertura de Contexto)', fontsize=11)
for bar, val in zip(bars, efic_sede_df['tiempo_promedio']):
    ax.text(val + 0.1, bar.get_y() + bar.get_height()/2, f'{val:.2f}s',
            va='center', fontsize=9)
ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'eficiencia_por_sede.png'), dpi=200)
plt.close(fig)
print("[OK] eficiencia_por_sede.png")

# Hora pico vs no pico
logs['hora'] = pd.to_datetime(logs['timestamp']).dt.hour
logs['periodo'] = logs['hora'].apply(lambda h: 'Hora pico (10-12h)' if 10 <= h <= 12 else 'Fuera de pico')

fig, ax = plt.subplots(figsize=(7, 4))
for i, (periodo, grupo) in enumerate(logs.groupby('periodo')):
    color = '#E74C3C' if 'pico' in periodo else '#2E6E9E'
    ax.hist(grupo['tiempo_segundos'], bins=30, alpha=0.7, color=color, label=periodo, edgecolor='white')
ax.axvline(x=8.0, color='black', linestyle='--', linewidth=1.5, label='Umbral RNF-01 (8s)')
ax.set_xlabel('Tiempo de registro (segundos)')
ax.set_ylabel('Frecuencia')
ax.set_title('Distribucion de tiempos: hora pico vs. fuera de pico')
ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'pico_vs_no_pico.png'), dpi=200)
plt.close(fig)
print("[OK] pico_vs_no_pico.png")

# ============================================================
# ESCENARIO 9-12: Incidentes por modulo (contexto)
# ============================================================
conteo_modulo = incidentes['modulo'].value_counts()
fig, ax = plt.subplots(figsize=(7, 4.2))
counts = conteo_modulo.sort_values(ascending=True)
bars = ax.barh(counts.index, counts.values, color='#2E6E9E')
ax.set_xlabel('Numero de incidentes reportados (2025)')
ax.set_title('Distribucion de incidentes por modulo - MediSalud HIS', fontsize=11)
for bar, val in zip(bars, counts.values):
    ax.text(val + 5, bar.get_y() + bar.get_height()/2, str(val), va='center', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, 'incidentes_por_modulo.png'), dpi=200)
plt.close(fig)
print("[OK] incidentes_por_modulo.png")

# ============================================================
# EXPORTAR JSON COMPLETO DE METRICAS
# ============================================================
salida = {
    'metricas': metricas,
    'eficiencia_por_sede': efic_sede.round(2).to_dict(),
    'efectividad_por_sede': efect_sede.set_index('sede')['tasa_completitud'].round(4).to_dict(),
    'csat_por_rol': csat_rol.round(2).to_dict(),
    'total_logs_hce': total_logs,
    'total_encuestas': len(encuesta),
    'total_incidentes': len(incidentes),
}

os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'dashboards'), exist_ok=True)
with open(os.path.join(os.path.dirname(__file__), '..', 'dashboards', 'indicadores.json'), 'w', encoding='utf-8') as f:
    json.dump(salida, f, indent=2, ensure_ascii=False, default=str)
print("[OK] dashboards/indicadores.json")

# ============================================================
# IMPRIMIR RESUMEN DE METRICAS (para consola)
# ============================================================
print("\n" + "="*60)
print("RESUMEN DE METRICAS ISO/IEC 25022 - MediSalud HIS")
print("="*60)
for nombre, m in metricas.items():
    estado = 'CUMPLE' if m['cumple'] else 'NO CUMPLE'
    print(f"  {nombre:.<30} {m['valor']} {m['unidad']} (umbral: {m['umbral']}) -> {estado}")

print(f"\nEficiencia por sede:")
for sede, val in efic_sede.sort_values().items():
    print(f"  {sede:.<15} {val:.2f}s")

print(f"\nCSAT por rol:")
for rol, val in csat_rol.sort_values().items():
    print(f"  {rol:.<25} {val:.2f}/5")

print(f"\n  Efectividad global: {efectividad:.4f} ({completadas}/{total_logs})")
print(f"  Eficiencia global:  {eficiencia:.2f}s")
print(f"  CSAT normalizado:   {csat_norm:.4f}")
print(f"  Tasa error fact.:   {libertad_riesgo:.4f}")
print(f"  Cobertura contexto: {cobertura:.4f}")
print("="*60)
