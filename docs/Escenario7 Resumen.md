# Escenario 7 — Obtención y Validación de Datos

**Asignatura:** Aseguramiento de la Calidad del Software — NRC 30733
**Docente:** Ing. Diego Gamboa
**Grupo 7 — Calidad en Uso**
**Integrantes:** Kevin Amaguaña, Jairo Bonilla, Darwin Panchez, Eduardo Mortensen
**Caso de estudio:** Red Hospitalaria MediSalud Ecuador (MediSalud HIS)

## Descripción general

Este escenario aborda la **generación, identificación y validación** de las fuentes de datos
necesarias para alimentar el cálculo automático de las cinco métricas ISO/IEC 25022
diseñadas en el Escenario 6. El propósito es preparar los archivos de datos base que
alimentarán la automatización en el Escenario 8, garantizando que estén libres de nulos
críticos, duplicados y valores fuera de rango.

## Qué se realizó

1. **Identificación de tres fuentes de datos** para el programa de medición:
   - `data/logs_hce.csv` (3,150 registros): logs transaccionales del módulo HCE, generados
     por `generar_logs_hce.py`, simulando 5 días hábiles en 5 sedes con degradación en
     horas pico (10–12h).
   - `data/encuesta_satisfaccion.csv` (150 respuestas): encuestas CSAT generadas por
     `generar_encuestas.py`, con sesgo intencional por rol (médicos con puntajes bajos).
   - `data/incidentes_2025_iso_25022.csv` (3,006 incidentes): dataset real de incidentes
     reportados en 2025, utilizado desde el Escenario 2.

2. **Validación de datos** (`01_validacion_datos.py`) con tres verificaciones:
   - Valores nulos en columnas críticas: 0 nulos encontrados
   - Tiempos fuera de rango (<0s o >120s): 0 registros
   - Duplicados en `evento_id`: 0 duplicados

3. **Análisis exploratorio de los datos** con 4 gráficos generados por
   `generar_evidencia_escenarios.py`:
   - Histograma de tiempos de registro HCE + boxplot por sede
   - Distribución hora pico vs. fuera de pico
   - Efectividad (completitud) por sede
   - Distribución CSAT + promedio por rol de usuario

4. **Preguntas de discusión** sobre: riesgos de datos sintéticos, utilidad del sesgo
   intencional en encuestas CSAT, y verificaciones adicionales necesarias con datos de
   producción.

5. **Informe final en LaTeX** (`informe_escenario7.tex` / `.pdf`), con carátula ESPE, 4
   figuras embebidas, tablas de validación y conclusiones.

## Estructura de archivos

```
scripts/
├── generar_logs_hce.py            # Generador de logs transaccionales sintéticos
├── generar_encuestas.py           # Generador de encuestas CSAT
├── 01_validacion_datos.py         # Script de validación de datos
└── generar_evidencia_escenarios.py # Generador de todos los gráficos

data/
├── logs_hce.csv                   # 3,150 registros de HCE
├── encuesta_satisfaccion.csv      # 150 respuestas CSAT
└── incidentes_2025_iso_25022.csv  # 3,006 incidentes (dataset original)

reportes/
├── informe_escenario7.tex         # Fuente LaTeX del informe
├── informe_escenario7.pdf         # Informe compilado (entregable)
└── img/
    ├── distribucion_tiempos_hce.png  # Histograma + boxplot
    ├── pico_vs_no_pico.png           # Hora pico vs fuera de pico
    ├── efectividad_por_sede.png      # Completitud por sede
    └── encuesta_csat.png             # Distribución CSAT + por rol
```

## Cómo reproducir el análisis

```bash
python scripts/generar_logs_hce.py
python scripts/generar_encuestas.py
python scripts/01_validacion_datos.py
python scripts/generar_evidencia_escenarios.py
```

## Cómo compilar el informe

```bash
pdflatex informe_escenario7.tex
pdflatex informe_escenario7.tex   # segunda pasada para el índice
```

## Principales hallazgos

| Indicador | Valor |
|---|---|
| Total de logs HCE generados | 3,150 |
| Total de encuestas CSAT | 150 |
| Nulos encontrados | 0 |
| Duplicados encontrados | 0 |
| Valores fuera de rango | 0 |
| CSAT promedio médicos | 2.22/5 |
| CSAT promedio pacientes | 4.14/5 |
| % registros en hora pico (10–12h) | ~25% |
| Tasa de completitud global (Efectividad) | 96.51% |

## Conclusión del escenario

Al finalizar este escenario, el equipo cuenta con conjuntos de datos base (logs de HCE,
encuestas CSAT e incidentes) validados, limpios y libres de valores atípicos perjudiciales.
El análisis exploratorio confirmó empíricamente los patrones esperados: degradación en horas
pico, baja satisfacción de médicos, y consistencia entre sedes. Estos datos constituyen un
prerrequisito técnico ineludible para el cálculo automático de las métricas ISO/IEC 25022 en
el Escenario 8.
