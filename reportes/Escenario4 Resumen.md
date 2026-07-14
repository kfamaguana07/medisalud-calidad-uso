# Escenario 4 — Identificación de Atributos de Calidad en Uso

**Asignatura:** Aseguramiento de la Calidad del Software — NRC 30733
**Docente:** Ing. Diego Gamboa
**Grupo 7 — Calidad en Uso**
**Integrantes:** Kevin Amaguaña, Jairo Bonilla, Darwin Panchez, Eduardo Mortensen
**Caso de estudio:** Red Hospitalaria MediSalud Ecuador (MediSalud HIS)

## Descripción general

Este escenario tiene como objetivo operacionalizar los procesos de negocio abstractos de
MediSalud HIS en **tareas medibles y contextos de uso explícitos**, siguiendo el modelo
**Usuario–Tarea–Contexto** exigido por la norma ISO/IEC 25022. Es el paso previo
indispensable antes de diseñar métricas formales: sin saber *qué* medir, *a quién* y *en qué
condiciones*, ninguna métrica tiene validez.

## Qué se realizó

1. **Marco conceptual** del modelo Usuario–Tarea–Contexto de ISO/IEC 25022, explicando por
   qué la calidad en uso no puede medirse en abstracto y requiere especificar usuario, tarea
   e infraestructura.

2. **Selección de los tres procesos críticos** de MediSalud HIS, justificada con datos
   empíricos del Escenario 3 (% de incidentes por módulo):
   - Atención médica y registro de HCE (25.6% de incidentes)
   - Agendamiento de citas por el paciente (18.2%)
   - Facturación de consulta con seguro médico (14.2%)

3. **Tres fichas formales de Usuario–Tarea–Contexto** (UTC-01, UTC-02, UTC-03), cada una con:
   - Identificador, proceso de negocio, usuario primario y perfil
   - Tarea representativa y criterio de éxito
   - Contexto de uso (horario, sede, infraestructura, carga concurrente)
   - Atributos de calidad en uso vinculados y frecuencia estimada

4. **Tabla de cobertura** de las cinco características ISO/IEC 25022 por ficha, verificando
   que las tres fichas cubren Efectividad, Eficiencia, Satisfacción, Libertad de Riesgo y
   Cobertura de Contexto (esta última de forma transversal, por sede).

5. **Preguntas de discusión** con respuestas argumentadas, incluyendo la vinculación de la
   ficha UTC-03 con el incidente 1003 (Libertad de Riesgo) del Escenario 2.

6. **Informe final en LaTeX** (`informe_escenario4.tex` / `.pdf`), con carátula institucional
   ESPE, tabla de contenidos, tablas con `booktabs`, `tcolorbox` para ideas clave y
   conclusiones formales.

## Estructura de archivos

```
reportes/
├── informe_escenario4.tex         # Fuente LaTeX del informe
└── informe_escenario4.pdf         # Informe compilado (entregable)
```

## Cómo compilar el informe

```bash
pdflatex informe_escenario4.tex
pdflatex informe_escenario4.tex   # segunda pasada para el índice
```

## Principales hallazgos

| Indicador | Valor |
|---|---|
| Procesos críticos seleccionados | 3 |
| Fichas UTC elaboradas | 3 (UTC-01, UTC-02, UTC-03) |
| Características ISO 25022 cubiertas | 5/5 |
| Ficha con más atributos vinculados | UTC-01 (HCE): Eficiencia, Efectividad, Satisfacción |
| RNF vinculados directamente | RNF-01 (≤8s en HCE), RNF-03 (≤1% errores facturación) |
| Frecuencia estimada más alta | UTC-01: ~4,800 registros diarios en toda la red |

## Conclusión del escenario

Se ha logrado operacionalizar los procesos de negocio abstractos en tareas medibles y
contextos de uso explícitos. Este es el requisito indispensable exigido por la norma ISO/IEC
25022 antes de proceder a diseñar las métricas formales en el Escenario 6. Las fichas
garantizan que cada medición futura estará anclada a un usuario real, una tarea concreta y
un contexto operativo específico, evitando indicadores genéricos que enmascaran problemas
reales como los documentados en el Escenario 3.
