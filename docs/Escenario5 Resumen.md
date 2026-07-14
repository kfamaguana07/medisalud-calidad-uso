# Escenario 5 — Mapeo de Características de Calidad y Priorización

**Asignatura:** Aseguramiento de la Calidad del Software — NRC 30733
**Docente:** Ing. Diego Gamboa
**Grupo 7 — Calidad en Uso**
**Integrantes:** Kevin Amaguaña, Jairo Bonilla, Darwin Panchez, Eduardo Mortensen
**Caso de estudio:** Red Hospitalaria MediSalud Ecuador (MediSalud HIS)

## Descripción general

Este escenario construye la **matriz de mapeo** que vincula cada tarea definida en las fichas
Usuario–Tarea–Contexto del Escenario 4 con las cinco características de calidad en uso de
ISO/IEC 25022, y **prioriza** cuáles serán medidas en el programa de medición de MediSalud
HIS, garantizando que el programa sea sostenible y accionable desde la primera iteración.

## Qué se realizó

1. **Definición de criterios de priorización** basados en dos dimensiones ortogonales:
   - Impacto (1–5): severidad del efecto sobre la salud del paciente o el flujo de caja.
   - Frecuencia (1–5): número de ejecuciones diarias de la tarea en toda la red.
   - Puntuación: P = Impacto × Frecuencia, con tres niveles de prioridad.

2. **Matriz de mapeo Tarea–Característica–Prioridad** con 6 tareas priorizadas:
   - Prioridad 1 (P ≥ 15): Registro HCE, Agendamiento, Facturación, Adm. medicamentos.
   - Prioridad 2 (9 ≤ P < 15): Teleconsulta, Historial de laboratorio.
   - Las 4 tareas de Prioridad 1 concentran el 66.6% del volumen total de incidentes de 2025.

3. **Gráfico de priorización** (`img/priorizacion_tareas.png`), generado por el script
   `generar_evidencia_escenarios.py`, que visualiza la puntuación de cada tarea y el umbral
   de prioridad alta.

4. **Análisis de cobertura de características**, verificando que las tareas de Prioridad 1
   y 2 cubren las cinco características de ISO/IEC 25022.

5. **Preguntas de discusión** con argumentación sobre por qué no conviene medir todo desde
   el primer ciclo, la transversalidad de la Cobertura de Contexto, y por qué la
   Administración de medicamentos es Prioridad 1 pese a su menor volumen de incidentes
   (impacto clínico > volumen).

6. **Informe final en LaTeX** (`informe_escenario5.tex` / `.pdf`), con carátula ESPE, tabla
   de contenidos, figura embebida, tablas con `booktabs` y conclusiones formales.

## Estructura de archivos

```
reportes/
├── informe_escenario5.tex         # Fuente LaTeX del informe
├── informe_escenario5.pdf         # Informe compilado (entregable)
└── img/
    └── priorizacion_tareas.png    # Gráfico de priorización generado
```

## Cómo compilar el informe

```bash
pdflatex informe_escenario5.tex
pdflatex informe_escenario5.tex   # segunda pasada para el índice
```

## Principales hallazgos

| Indicador | Valor |
|---|---|
| Tareas priorizadas | 6 |
| Tareas de Prioridad 1 | 4 (Registro HCE, Agendamiento, Facturación, Adm. medicamentos) |
| Tareas de Prioridad 2 | 2 (Teleconsulta, Historial de laboratorio) |
| Puntuación máxima | 25 (Registro HCE y Agendamiento) |
| Características cubiertas (Prioridad 1+2) | 5/5 |
| % de incidentes cubiertos por Prioridad 1 | 66.6% |

## Conclusión del escenario

La elaboración de la matriz de mapeo con criterios cuantitativos de priorización permite
comprender que un programa de medición sostenible se construye de forma incremental. Al
priorizar las tareas de mayor impacto y frecuencia (Prioridad 1), MediSalud podrá enfocar
sus esfuerzos de calidad en las áreas que representan mayor riesgo y valor para la operación
y los usuarios finales, sin sobrecarga operativa que comprometa la viabilidad del programa.
