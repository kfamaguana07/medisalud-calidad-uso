# Escenario 3 — Comprensión del Modelo SQuaRE

**Asignatura:** Aseguramiento de la Calidad del Software — NRC 30733
**Docente:** Ing. Diego Gamboa
**Grupo 7 — Calidad en Uso**
**Integrantes:** Kevin Amaguaña, Jairo Bonilla, Darwin Panchez, Eduardo Mortensen
**Caso de estudio:** Red Hospitalaria MediSalud Ecuador (MediSalud HIS)

## Descripción general

Este escenario ubica a la norma **ISO/IEC 25022** dentro de la familia completa **ISO/IEC 25000
(SQuaRE)**, diferenciando el modelo de calidad (ISO/IEC 25010), la medición de calidad (ISO/IEC
25022) y el proceso de evaluación (ISO/IEC 25040). Además de la parte teórica del taller, este
grupo amplió el trabajo con un análisis empírico sobre datos reales de incidentes del sistema
MediSalud HIS, para sustentar con evidencia cuantitativa por qué la Calidad en Uso es el nivel de
evaluación más cercano a la experiencia real del usuario.

## Qué se realizó

1. **Investigación dirigida** sobre los tres niveles de calidad del modelo SQuaRE:
   - Calidad interna (análisis estático de código, ej. SonarQube)
   - Calidad externa (pruebas controladas, ej. JMeter)
   - Calidad en uso (experiencia real del usuario, ISO/IEC 25022)

2. **Mapa conceptual** de la familia ISO/IEC 25000, mostrando cómo se relacionan las normas
   25000, 25010, 25022 y 25040, y cómo los tres niveles de calidad se apoyan entre sí.

3. **Aplicación al caso MediSalud HIS**, con un ejemplo concreto para cada nivel de calidad
   (facturación para calidad interna, portal de citas para calidad externa, registro de HCE para
   calidad en uso).

4. **Análisis de datos reales** (`analisis_incidentes.py`) sobre el dataset de 3,000 incidentes
   reportados en 2025, para verificar en la práctica el argumento del escenario:
   - Distribución de incidentes por módulo, rol de usuario y sede.
   - Extracción de los tiempos mencionados en el texto libre de los incidentes (regex) para
     contrastarlos contra el requerimiento no funcional **RNF-01** (registro de nota de evolución
     clínica en máximo 8 segundos).
   - Resultado: el 100% de los incidentes analizados de este tipo incumplen el umbral, con un
     tiempo promedio de 22.1 segundos, muy por encima de lo exigido.

5. **Informe final en LaTeX** (`informe_escenario3.tex` / `.pdf`), con la misma carátula y formato
   institucional usados en el resto del taller (logo ESPE, datos de asignatura y equipo), que
   documenta todo lo anterior de forma detallada.

## Estructura de archivos

```
.
├── informe_escenario3.tex         # Fuente LaTeX del informe
├── informe_escenario3.pdf         # Informe compilado (entregable)
├── analisis_incidentes.py         # Script de análisis del dataset
├── incidentes_2025_iso_25022.csv  # Dataset de incidentes (no incluido en el repo público)
├── incidentes_por_modulo.png      # Gráfico generado por el script
├── incidentes_por_sede.png        # Gráfico generado por el script
└── espe_logo.png                  # Logo institucional usado en la carátula
```

## Cómo reproducir el análisis

```bash
pip install pandas matplotlib --break-system-packages
python3 analisis_incidentes.py
```

Esto regenera las tablas de conteo (por módulo, rol y sede) y los dos gráficos usados en el
informe. Requiere el archivo `incidentes_2025_iso_25022.csv` en el mismo directorio.

## Cómo compilar el informe

```bash
pdflatex informe_escenario3.tex
pdflatex informe_escenario3.tex   # segunda pasada para el índice
```

Requiere `pdflatex` (TeX Live) y los paquetes `tikz`, `tcolorbox`, `booktabs`, `tabularx`, entre
otros estándar de una distribución LaTeX completa.

## Principales hallazgos

| Indicador | Valor |
|---|---|
| Total de incidentes analizados | 3,000 |
| Módulo con más incidentes | HCE (769, 25.6%) |
| Sede con más incidentes | Quito (1,035) |
| Incidentes de "nota de evolución tarda Xs" | 63 |
| Tiempo promedio reportado | 22.1 s |
| Umbral definido en RNF-01 | 8.0 s |
| % de incumplimiento de RNF-01 | 100% |

## Conclusión del escenario

La calidad interna y la calidad externa, evaluadas de forma aislada, no bastan para detectar
problemas que solo emergen en producción, con usuarios reales y contexto real de uso. El análisis
del dataset de incidentes confirma que ISO/IEC 25022 (Calidad en Uso) es el instrumento que
realmente expone estas brechas, reforzando el argumento central del taller: pasar de una cultura
de decisiones basada en percepción a una basada en evidencia medible.
