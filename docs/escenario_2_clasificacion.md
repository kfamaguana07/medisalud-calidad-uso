# Taller – ISO/IEC 25022: Comprensión y Clasificación de Incidentes

## Información General

**Asignatura:** Aseguramiento de la Calidad del Software
**Tema:** Comprensión de la norma ISO/IEC 25022

**Integrantes:**
- Jairo Bonilla
- Kevin Amaguañá
- Edwin Panches
- Eduardo Mortencen

---

# Escenario 2: Comprensión de ISO/IEC 25022

## Paso 2. Tabla de Clasificación de Incidentes

A partir del fragmento representativo de incidentes del dataset `data/incidentes_2025_iso_25022.csv`, se presenta la clasificación de cada caso de acuerdo con las cinco características de calidad en uso definidas por la norma **ISO/IEC 25022**:

| ID | Característica | Justificación Técnica |
|----|---------------|----------------------|
| **1001** | **Eficiencia** | La nota de evolución se guarda correctamente (la tarea se completa), pero tarda 22 segundos, muy por encima del umbral de 8 segundos definido en RNF-01. El problema es de recursos (tiempo) utilizados para lograr el objetivo, no de fracaso del objetivo. |
| **1002** | **Efectividad** | El usuario no logra agendar la cita tras 3 intentos. El objetivo principal de la tarea no puede alcanzarse, lo que afecta directamente la completitud y precisión con que el usuario cumple su meta. |
| **1003** | **Libertad de Riesgo** | La factura duplicada al reintentar el pago genera un riesgo económico tanto para el paciente (doble cobro) como para la organización (discrepancias financieras, reembolsos). No se trata de un problema de efectividad (la factura se emite), sino del riesgo financiero asociado. |
| **1004** | **Efectividad** | La videollamada se corta a los 4 minutos, interrumpiendo la teleconsulta antes de que el paciente y el médico puedan completar la atención. El objetivo de la tarea no se alcanza en su totalidad. |
| **1005** | **Libertad de Riesgo** | La exposición breve de datos de otro paciente constituye un riesgo de privacidad y seguridad de la información. Aunque el médico logra visualizar datos (efectividad), el problema principal es la violación de confidencialidad y el incumplimiento regulatorio de protección de datos sensibles en salud. |
| **1006** | **Efectividad** | El formulario confuso provoca que el usuario abandone el registro antes de completarlo. La tarea de agendamiento no se finaliza, lo que constituye una falla de efectividad: el usuario no alcanza su objetivo. |

---

## Análisis Crítico: Discusión del Incidente 1005

### Pregunta (del taller)

**¿Por qué corresponde principalmente a Libertad de Riesgo y no a Efectividad, a pesar de tratarse también de un error del sistema?**

### Análisis

El incidente **1005** describe que "Datos de otro paciente visibles brevemente" durante el uso del módulo HCE por parte de un médico. A primera vista, podría clasificarse como _Efectividad_ porque el sistema muestra información incorrecta (datos de otro paciente), lo que constituye una imprecisión en la tarea. Sin embargo, el impacto más grave no es la inexactitud momentánea, sino la **exposición de datos sensibles de salud** de un tercero sin su consentimiento.

La _Libertad de Riesgo_ mide el grado en que el sistema mitiga riesgos económicos, de salud, de seguridad o ambientales. En este caso:

1. **Riesgo de privacidad**: Se viola la confidencialidad del historial clínico del paciente cuyos datos fueron expuestos, lo que contraviene normativas de protección de datos (Ley de Protección de Datos Personales en Ecuador, estándares internacionales como HIPAA).

2. **Riesgo legal**: La exposición de información clínica sin autorización puede derivar en sanciones legales, demandas y pérdida de licencias operativas para MediSalud.

3. **Riesgo reputacional**: La confianza de los pacientes en el sistema se erosiona si perciben que sus datos pueden ser vistos por otros.

Aunque el sistema sigue siendo _efectivo_ en el sentido de que el médico logra visualizar información clínica (su objetivo inmediato de consultar datos se cumple), el costo asociado a esa efectividad es la exposición de datos ajenos. El problema central no es que la tarea falle, sino que el sistema introduce un **riesgo inaceptable** durante su ejecución normal.

Por lo tanto, el incidente 1005 corresponde principalmente a **Libertad de Riesgo**, porque el riesgo de privacidad y las consecuencias legales/reputacionales dominan sobre cualquier consideración de efectividad de la tarea.

---

## 3. Preguntas de Discusión

### 1. ¿Puede un sistema ser efectivo pero no eficiente? Dé un ejemplo del caso MediSalud.

**Respuesta:**

Sí. Un sistema puede permitir que los usuarios completen correctamente una tarea y, por tanto, ser **efectivo**, pero al mismo tiempo requerir un tiempo o recursos excesivos para lograrlo, lo que afecta su **eficiencia**.

**Ejemplo:**

El incidente **1001** del dataset lo ilustra perfectamente. La nota de evolución clínica **se guarda correctamente** (efectividad: el médico logra su objetivo), pero tarda **22 segundos**, muy por encima del umbral de 8 segundos definido por el requerimiento RNF-01. Durante una consulta de 15 minutos, una demora de 14 segundos adicionales por nota puede acumularse significativamente a lo largo de la jornada, afectando la productividad del médico y el tiempo de espera de los pacientes.

---

### 2. ¿Por qué la Cobertura de Contexto es especialmente relevante para una red hospitalaria con sedes en cinco ciudades distintas?

**Respuesta:**

La **Cobertura de Contexto** evalúa si un sistema mantiene un nivel adecuado de calidad en diferentes condiciones de uso y entornos operativos. Para MediSalud, que opera en Quito, Guayaquil, Cuenca, Ambato y Manta, esta característica es crítica porque:

1. **Infraestructura heterogénea**: Cada sede puede tener diferente calidad de conexión a internet, hardware, y capacidad de cómputo. Un sistema que funciona bien en Quito podría degradarse en Manta si no está diseñado para adaptarse a contextos variables.

2. **Carga de usuarios desigual**: Quito y Guayaquil concentran la mayor cantidad de pacientes y personal médico. Una métrica que mida solo el desempeño promedio global podría ocultar que en las sedes más grandes el sistema se degrada en horas pico.

3. **Procesos locales**: Cada ciudad puede tener variaciones en los flujos de atención médica, horarios de consulta y perfiles de pacientes. La Cobertura de Contexto garantiza que el sistema se comporte consistentemente sin importar estas diferencias.

4. **Equidad en la atención**: Los pacientes de todas las sedes merecen el mismo nivel de calidad en el servicio. Sin medir Cobertura de Contexto, MediSalud no podría detectar si una sede está recibiendo una experiencia significativamente peor que otra.

---

## Conclusión

La clasificación de los incidentes conforme a la **ISO/IEC 25022** permite identificar cómo cada problema impacta la calidad en uso del sistema desde diferentes perspectivas. El incidente 1001 evidencia una falla de _eficiencia_ (tarea completada pero con recursos excesivos), los incidentes 1002, 1004 y 1006 afectan la _efectividad_ (tareas no completadas), y los incidentes 1003 y 1005 representan principalmente _libertad de riesgo_ (consecuencias económicas y de privacidad). Este análisis facilita priorizar acciones de mejora orientadas a incrementar la calidad del software y garantizar un funcionamiento confiable, efectivo y seguro en todas las sedes donde opera MediSalud.
