# Taller – ISO/IEC 25022: Comprensión y Clasificación de Incidentes

## Información General

**Asignatura:** Calidad de Software  
**Tema:** Comprensión de la norma ISO/IEC 25022

**Integrantes:**

- Jairo Bonilla
- Kevin Amaguañá
- Edwin Panches
- Eduardo Mortencen

---

# Escenario 2: Comprensión de ISO/IEC 25022

## Paso 2. Tabla de Clasificación de Incidentes

A partir de los incidentes obtenidos durante la ejecución del escenario de evaluación, se presenta la clasificación y la justificación técnica de cada caso de acuerdo con las características de calidad en uso definidas por la norma **ISO/IEC 25022**.

| ID | Característica | Justificación Técnica |
|----|---------------|----------------------|
| **1001** | **Efectividad** | El paciente no consigue completar el proceso de agendamiento después de varios intentos, por lo que el objetivo principal de la tarea no puede alcanzarse correctamente. |
| **1002** | **Efectividad** | La orden médica no llega al módulo de farmacia debido a una falla de sincronización, impidiendo completar adecuadamente el proceso asistencial previsto. |
| **1003** | **Libertad de Riesgo** | La asignación del mismo turno a dos pacientes diferentes genera inconsistencias operativas y posibles afectaciones en la atención médica, introduciendo riesgos para la organización y los usuarios. |
| **1004** | **Efectividad** | La información registrada por enfermería no está disponible para el médico durante la consulta, impidiendo disponer de todos los datos necesarios para realizar correctamente la atención. |
| **1005** | **Eficiencia** | El tiempo de respuesta del portal de citas supera el umbral esperado durante horas de alta demanda, incrementando el tiempo necesario para completar la tarea y disminuyendo el desempeño del sistema. |
| **1006** | **Libertad de Riesgo** | La imposibilidad de validar la firma electrónica del médico compromete la autenticidad e integridad del registro clínico, generando riesgos legales y de trazabilidad documental. |

---

# 2. Análisis Crítico: Discusión del Incidente 1006

## Pregunta

**¿Por qué corresponde principalmente a Libertad de Riesgo y no a Efectividad, a pesar de tratarse también de un error del sistema?**

### Análisis

El incidente se clasifica principalmente como **Libertad de Riesgo** porque el impacto más importante no consiste únicamente en que una tarea no pueda finalizar correctamente, sino en las consecuencias que produce sobre la confiabilidad y la validez legal de la información clínica.

La firma electrónica garantiza la autenticidad del profesional responsable, la integridad del documento y la trazabilidad del historial médico. Cuando esta validación falla, el sistema genera un riesgo significativo desde el punto de vista legal, normativo y de seguridad de la información. Aunque el proceso de cierre de la consulta también resulta afectado, la principal consecuencia es el riesgo asociado a la pérdida de confianza en los registros clínicos y al posible incumplimiento de requisitos regulatorios.

---

# 3. Preguntas de Discusión

## 1. ¿Puede un sistema ser efectivo pero no eficiente? Dé un ejemplo del caso MediSalud.

### Respuesta

Sí. Un sistema puede permitir que los usuarios completen correctamente una tarea y, por tanto, ser **efectivo**, pero al mismo tiempo requerir un tiempo o una cantidad de recursos excesivos para lograrlo, lo que afecta su **eficiencia**.

### Ejemplo

En el caso de **MediSalud**, el incidente **1005** muestra esta situación. El portal de citas continúa permitiendo que el paciente realice el proceso de agendamiento; sin embargo, durante las horas de mayor demanda el tiempo de respuesta supera los valores esperados. Aunque la tarea puede completarse, el elevado tiempo de espera reduce el desempeño del sistema y afecta la experiencia del usuario, representando un problema de eficiencia.

---

## 2. ¿Por qué la Cobertura de Contexto es especialmente relevante para una red hospitalaria con sedes en cinco ciudades distintas?

### Respuesta

La **Cobertura de Contexto** es una característica fundamental porque evalúa si un sistema mantiene un nivel adecuado de calidad en diferentes condiciones de uso y entornos operativos.

En el caso de **MediSalud**, los incidentes registrados provienen de sedes ubicadas en **Quito, Guayaquil, Cuenca y Manta**, lo que evidencia que el sistema es utilizado en ambientes con diferentes condiciones de infraestructura, conectividad, carga de usuarios y procesos clínicos.

Evaluar la cobertura de contexto permite comprobar que las funcionalidades del sistema mantienen un comportamiento consistente independientemente de la sede donde se utilicen. Esto contribuye a garantizar que la atención médica, la gestión de citas y el manejo de la historia clínica electrónica ofrezcan el mismo nivel de calidad, seguridad y rendimiento para todos los usuarios de la red hospitalaria.

---

# Conclusión

La clasificación de los incidentes conforme a la **ISO/IEC 25022** permite identificar cómo cada problema impacta la calidad en uso del sistema desde diferentes perspectivas. Mientras algunos incidentes afectan directamente la efectividad de las tareas, otros representan riesgos para la organización o disminuyen la eficiencia del servicio. Este análisis facilita priorizar acciones de mejora orientadas a incrementar la calidad del software y garantizar un funcionamiento confiable en todas las sedes donde opera MediSalud.