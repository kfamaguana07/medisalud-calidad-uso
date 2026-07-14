# 1.2.3 Paso 3: Análisis dirigido del caso

### Tabla 1.1: Matriz de análisis inicial del caso MediSalud

| Pregunta guía | Respuesta del grupo |
| :--- | :--- |
| **¿Cuáles son los 3 procesos más críticos del negocio?** | (1) Atención médica y registro de historia clínica (HCE), ya que un retraso puede afectar decisiones clínicas urgentes. (2) Facturación y gestión de seguros/reaseguros, debido a los errores de doble facturación que afectan el flujo de caja. (3) Telemedicina y seguimiento remoto, por el abandono de sesiones y las caídas de conexión que comprometen la continuidad de la atención. |
| **¿Qué usuarios se ven más afectados por la problemática actual?** | Los médicos tratantes, por la lentitud del módulo de HCE en horas pico; los pacientes, por las demoras al agendar citas y el abandono de sesiones de telemedicina; y el personal de admisión/facturación, por los errores de doble cobro que generan reprocesos y reclamos. |
| **¿Qué evidencia tiene hoy MediSalud sobre la calidad de su software?** | Únicamente evidencia de disponibilidad de infraestructura (uptime) de los servidores, reportada por el área de TI. No existen métricas relacionadas con la experiencia real de uso del sistema. |
| **¿Qué evidencia le falta?** | Datos objetivos sobre efectividad (si los usuarios logran completar sus tareas), eficiencia (tiempos reales de registro de HCE, agendamiento, facturación), satisfacción de médicos y pacientes, libertad de riesgo (errores de facturación, exposición de datos sensibles) y cobertura de contexto (si el sistema funciona igual en las cinco ciudades donde opera la red). En resumen, falta un programa de medición de Calidad en Uso basado en ISO/IEC 25022. |

-----

# Preguntas de Discusión — Escenario 1
 
**1. ¿Por qué la disponibilidad de servidores (uptime) no es suficiente para afirmar que un sistema tiene buena calidad en uso?**
Porque el uptime solo indica que la infraestructura está técnicamente operativa, pero no dice nada sobre si los usuarios reales pueden cumplir sus objetivos de forma efectiva, eficiente y satisfactoria. Un servidor puede estar "arriba" el 100% del tiempo y aun así el sistema puede ser lento, confuso, inseguro o poco confiable para quien lo usa (por ejemplo, un médico tardando 22 segundos en guardar una nota clínica). El uptime mide disponibilidad técnica, no experiencia de uso.
 
**2. ¿Qué diferencia existe entre la calidad interna, la calidad externa y la calidad en uso de un producto software?**
- **Calidad interna:** se mide sobre el código y la arquitectura del sistema, de forma estática, sin ejecutarlo (por ejemplo, complejidad ciclomática medida con SonarQube).
- **Calidad externa:** se mide sobre el comportamiento observable del sistema en ejecución, pero en un entorno controlado o de pruebas (por ejemplo, pruebas de carga con JMeter simulando usuarios concurrentes).
- **Calidad en uso:** se mide en producción, observando a usuarios reales realizando tareas reales en su contexto real de trabajo (por ejemplo, el tiempo que tarda un médico en registrar una nota clínica durante una consulta real). Es el nivel más cercano al negocio y al paciente.

**3. En el caso de MediSalud, ¿qué stakeholder se beneficiaría más de un programa de medición de calidad en uso: el paciente, el médico o la gerencia? Justifique.**
Los tres se benefician, pero de forma distinta:
- El **médico** gana en eficiencia y reduce el riesgo de errores clínicos por lentitud del sistema.
- El **paciente** gana en satisfacción y confianza (menos abandono en telemedicina, agendamiento más simple).
- La **gerencia** es quizás la más beneficiada de forma estratégica, porque hoy toma decisiones "por percepción" y el programa le da evidencia objetiva para priorizar inversiones de TI, negociar con aseguradoras y cumplir objetivos de negocio (reducir tiempos de HCE, bajar errores de facturación, aumentar finalización de teleconsultas). Sin datos, la gerencia no puede gestionar la calidad; con ellos, puede tomar decisiones basadas en evidencia en lugar de suposiciones.

-----

### Conclusiones Parciales

Este primer escenario estableció el marco de trabajo del taller y evidenció que las decisiones de TI en MediSalud Ecuador carecen de sustento medible, apoyándose únicamente en la disponibilidad técnica (uptime) sin considerar la experiencia real del usuario. Se identificaron los tres procesos más críticos (registro de HCE, facturación y telemedicina), los usuarios más afectados (médicos, pacientes y personal de admisión) y las brechas de evidencia que el programa de medición basado en ISO/IEC 25022 deberá cerrar. Los escenarios siguientes dotarán al equipo del marco normativo y las herramientas necesarias para implementar un sistema de medición de Calidad en Uso que transforme la cultura de "percepción" a una cultura de decisiones basadas en datos observables.