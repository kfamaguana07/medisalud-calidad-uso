# Escenario 8 — Automatización de la Medición de Calidad en Uso

**Asignatura:** Aseguramiento de la Calidad del Software — NRC 30733
**Docente:** Ing. Diego Gamboa
**Grupo 7 — Calidad en Uso**
**Integrantes:** Kevin Amaguaña, Jairo Bonilla, Darwin Panchez, Eduardo Mortensen
**Caso de estudio:** Red Hospitalaria MediSalud Ecuador (MediSalud HIS)

## Descripción general

Este escenario construye un **pipeline automatizado en Python** que calcula las cinco
métricas ISO/IEC 25022 del catálogo de MediSalud (Escenario 6), partiendo de los datos
validados en el Escenario 7. Genera un archivo de indicadores en formato JSON reutilizable
para tableros de control (dashboards) e integra el cálculo en un flujo de **Integración
Continua** mediante GitHub Actions.

## Qué se realizó

1. **Pipeline ETL (Extract–Transform–Load)** implementado en Python/Pandas:
   - `metricas_iso25022.py`: módulo central con funciones independientes para cada métrica.
   - `exportar_reporte.py`: exporta los resultados consolidados a JSON.
   - `generar_evidencia_escenarios.py`: genera todos los gráficos de evidencia.

2. **Cálculo automatizado de las 5 métricas**, con los siguientes resultados:

   | Métrica | Valor | Umbral | Estado |
   |---|---|---|---|
   | M-01 Efectividad | 0.9651 | ≥ 0.95 | CUMPLE |
   | M-02 Eficiencia | 7.43s | ≤ 8.0s | CUMPLE |
   | M-03 Satisfacción | 0.7107 | ≥ 0.80 | NO CUMPLE |
   | M-04 Libertad de Riesgo | 0.0501 | ≤ 0.01 | NO CUMPLE |
   | M-05 Cobertura Contexto | 0.9805 | ≥ 0.90 | CUMPLE |

3. **Dashboard de métricas** (`img/dashboard_metricas.png`): visualización automática con
   barras verdes (cumple) y rojas (no cumple), incluyendo valor, unidad y estado.

4. **Desagregación por sede** (Cobertura de Contexto):
   - Guayaquil: 7.37s, Cuenca: 7.40s, Quito: 7.43s, Ambato: 7.48s, Manta: 7.52s
   - Variación máxima entre sedes: < 2% → alta homogeneidad.

5. **Desagregación por rol** (Satisfacción CSAT):
   - Médico: 2.22/5 (NO CUMPLE), Enfermería: 4.06/5, Paciente: 4.14/5, Admisión: 4.17/5
   - El CSAT global (3.55/5) enmascara la brecha crítica de los médicos.

6. **Integración Continua** (`.github/workflows/medicion_calidad.yml`):
   - Trigger: cada lunes a las 06:00 UTC (cron) o manual (workflow_dispatch).
   - Pasos: checkout → instalación → cálculo → exportación → upload artifact.

7. **Informe final en LaTeX** (`informe_escenario8.tex` / `.pdf`), con carátula ESPE,
   dashboard embebido, tablas de resultados con colores, y 3 preguntas de discusión.

## Estructura de archivos

```
scripts/
├── metricas_iso25022.py           # Módulo de cálculo de métricas
├── exportar_reporte.py            # Exportación a JSON
└── generar_evidencia_escenarios.py # Generador de gráficos

.github/workflows/
└── medicion_calidad.yml           # Workflow de GitHub Actions

dashboards/
└── indicadores.json               # Reporte JSON exportado

reportes/
├── informe_escenario8.tex         # Fuente LaTeX del informe
├── informe_escenario8.pdf         # Informe compilado (entregable)
└── img/
    ├── dashboard_metricas.png     # Dashboard visual de métricas
    ├── eficiencia_por_sede.png    # Tiempo promedio por sede
    └── pico_vs_no_pico.png       # Hora pico vs fuera de pico
```

## Cómo reproducir el análisis

```bash
python scripts/generar_logs_hce.py
python scripts/generar_encuestas.py
python scripts/metricas_iso25022.py
python scripts/exportar_reporte.py
python scripts/generar_evidencia_escenarios.py
```

## Principales hallazgos

| Indicador | Valor |
|---|---|
| Métricas calculadas automáticamente | 5 |
| Métricas que cumplen umbral | 3/5 (Efectividad, Eficiencia, Cobertura) |
| Métricas que NO cumplen umbral | 2/5 (Satisfacción, Libertad de Riesgo) |
| Tasa de errores de facturación | 5.01% (~5× el umbral RNF-03 de 1%) |
| CSAT médicos | 2.22/5 (significativamente debajo del umbral 4.0/5) |
| Variación entre sedes | < 2% (alta Cobertura de Contexto) |
| Formato de salida | JSON (dashboards/indicadores.json) |
| CI/CD | GitHub Actions (cron semanal) |

## Conclusión del escenario

Se ha automatizado por completo el cálculo de las cinco métricas de calidad en uso,
transformando las fórmulas normativas abstractas de ISO/IEC 25022 en código Python
ejecutable, reproducible y auditable. El pipeline reveló que **2 de 5 métricas no cumplen**
sus umbrales (Satisfacción y Libertad de Riesgo), proporcionando evidencia cuantitativa
para priorizar acciones de mejora. La integración con GitHub Actions convierte el programa
en un proceso continuo, sentando las bases para que MediSalud abandone la gestión basada en
"percepciones" y transite hacia una gobernanza de calidad basada en datos observables.
