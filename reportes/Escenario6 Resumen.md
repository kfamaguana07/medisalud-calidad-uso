# Escenario 6 — Diseño Formal de Métricas ISO/IEC 25022

**Asignatura:** Aseguramiento de la Calidad del Software — NRC 30733
**Docente:** Ing. Diego Gamboa
**Grupo 7 — Calidad en Uso**
**Integrantes:** Kevin Amaguaña, Jairo Bonilla, Darwin Panchez, Eduardo Mortensen
**Caso de estudio:** Red Hospitalaria MediSalud Ecuador (MediSalud HIS)

## Descripción general

Este escenario traduce las características de calidad en uso priorizadas en el Escenario 5 en
**métricas formales, reproducibles y accionables**, siguiendo la estructura de ficha estándar
definida por la norma ISO/IEC 25022. Cada métrica queda documentada con: propósito, fórmula,
variables, unidad, rango deseado, fuente de datos, frecuencia de medición y responsable.

## Qué se realizó

1. **Estructura de ficha de métrica** según ISO/IEC 25022, con 11 campos formales que
   garantizan la trazabilidad entre la métrica, la ficha UTC del Escenario 4 y los
   requerimientos no funcionales del caso de estudio.

2. **Catálogo de 5 métricas** (una por característica del modelo):

   | ID   | Característica       | Nombre                                | Fórmula               | Umbral      |
   |------|----------------------|---------------------------------------|------------------------|-------------|
   | M-01 | Efectividad          | Completitud de registro de HCE        | X = A / B              | ≥ 0.95      |
   | M-02 | Eficiencia           | Tiempo promedio de registro de HCE    | X = Σtᵢ / n            | ≤ 8.0s      |
   | M-03 | Satisfacción         | Índice de Satisfacción CSAT           | X = Σsᵢ / (N × 5)      | ≥ 0.80      |
   | M-04 | Libertad de Riesgo   | Tasa de errores de facturación        | X = Fₑ / Fₜ            | ≤ 0.01      |
   | M-05 | Cobertura Contexto   | Consistencia de eficiencia entre sedes| X = 1 - |Tmax-Tmin|/Tmax | ≥ 0.90   |

3. **Vinculación con RNFs**: M-02 se vincula con RNF-01 (≤8s de registro), M-04 con RNF-03
   (≤1% de errores de facturación). Las demás métricas definen umbrales propios basados en
   buenas prácticas.

4. **Preguntas de discusión** con argumentación sobre:
   - Por qué la Satisfacción requiere encuesta y no puede inferirse de logs
   - Limitaciones de la fórmula M-05 y propuesta de mejora (coeficiente de variación)
   - Trazabilidad bidireccional entre métricas, fichas UTC y RNFs

5. **Informe final en LaTeX** (`informe_escenario6.tex` / `.pdf`), con carátula ESPE, tablas
   formales para cada ficha de métrica, tabla resumen del catálogo y conclusiones.

## Estructura de archivos

```
reportes/
├── informe_escenario6.tex         # Fuente LaTeX del informe
└── informe_escenario6.pdf         # Informe compilado (entregable)
```

## Cómo compilar el informe

```bash
pdflatex informe_escenario6.tex
pdflatex informe_escenario6.tex   # segunda pasada para el índice
```

## Principales hallazgos

| Indicador | Valor |
|---|---|
| Métricas diseñadas | 5 (una por característica ISO 25022) |
| Métricas vinculadas a RNFs | 2 (M-02 → RNF-01, M-04 → RNF-03) |
| Fuentes de datos identificadas | 3 (logs HCE, encuestas CSAT, incidentes) |
| Frecuencias de medición | Semanal (M-01, M-02, M-05), Trimestral (M-03), Mensual (M-04) |
| Responsables definidos | 3 áreas (Calidad, TI/DevOps, Facturación) |

## Conclusión del escenario

Se ha construido un catálogo formal de 5 métricas que traduce los conceptos normativos
abstractos de ISO/IEC 25022 en instrumentos de medición concretos, reproducibles y
accionables. La trazabilidad entre métricas → fichas UTC → RNFs garantiza que cualquier
resultado fuera de rango pueda ser rastreado hasta su origen operativo y normativo,
facilitando la toma de decisiones informadas. Las fórmulas están listas para ser
implementadas como código ejecutable en el Escenario 8.
