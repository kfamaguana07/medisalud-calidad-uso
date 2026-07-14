**ASEGURAMIENTO DE LA CALIDAD DEL SOFTWARE** 

# **Taller Calidad de Uso** 

Medición de la Calidad en Uso mediante ISO/IEC 25022 

_Caso de estudio: Sistema de Historia Clínica Electrónica Red Hospitalaria MediSalud Ecuador_ 

**Marco de referencia:** ISO/IEC 25000 (SQuaRE) 

**Norma central:** ISO/IEC 25022 — Measurement of Quality in Use **Nivel:** Séptimo Semestre — Ingeniería de Software **Modalidad:** Taller práctico basado en caso de estudio empresarial 

Ing. Diego Leonardo Gamboa Safla Mgtr. 

Versión 1.0 



## **Ficha Técnica del Material** 

|**Asignatura**|Aseguramiento de la Calidad del Software|
|---|---|
|**Unidad temática**|Evaluación de la Calidad del Producto de Software — Modelo SQuaRE|
|**Norma aplicada**|ISO/IEC 25022:2016 — Measurement of Quality in Use|
|**Modalidad**|Presencial / En Línea|
|**Prerrequisitos**|Ingeniería de software|
|**Caso de estudio**|Sistema de Historia Clínica Electrónica (HCE) de una red hospitalaria<br>nacional|



# **Índice general** 

|**Presen**|**tación **|**General del Taller**|**8**|
|---|---|---|---|
|**Caso d**|**e Estu**|**dio: Red Hospitalaria MediSalud Ecuador**|**10**|
|**1. Intr**|**oducci**|**ón al Caso Empresarial**|**15**|
|1.1.|Parte|1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>15|
||1.1.1.|El rol del Ingeniero de Calidad en un contexto empresarial real . . .|. . .<br>15|
||1.1.2.|De la percepción a la evidencia . . . . . . . . . . . . . . . . . . . . .|. . .<br>15|
||1.1.3.|Presentación del equipo de trabajo . . . . . . . . . . . . . . . . . . .|. . .<br>15|
|1.2.|Parte|2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>16|
||1.2.1.|Paso 1: Creación del repositorio de trabajo<br>. . . . . . . . . . . . . .|. . .<br>16|
||1.2.2.|Paso 2: Instalación del entorno Python . . . . . . . . . . . . . . . . .|. . .<br>16|
||1.2.3.|Paso 3: Análisis dirigido del caso . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|**2. Co**|**mprens**|**ión de ISO/IEC 25022**|**18**|
|2.1.|Parte|1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>18|
||2.1.1.|¿Qué es ISO/IEC 25022?<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>18|
||2.1.2.|Las cinco características de Calidad en Uso . . . . . . . . . . . . . .|. . .<br>18|
||2.1.3.|Aplicación conceptual al caso MediSalud. . . . . . . . . . . . . . . .|. . .<br>19|
||2.1.4.|Estructura general de una métrica en ISO/IEC 25022<br>. . . . . . . .|. . .<br>19|
|2.2.|Parte|2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>20|
|**3. Co**|**mprens**|**ión del Modelo SQuaRE**|**22**|
|3.1.|Parte|1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>22|
||3.1.1.|¿Qué es SQuaRE? . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>22|
||3.1.2.|Relación entre ISO/IEC 25010 y 25022. . . . . . . . . . . . . . . . .|. . .<br>22|
|3.2.|Parte|2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>23|
|**4. Ide**|**ntifcac**|**ión de Atributos de Calidad en Uso**|**25**|
|4.1.|Parte|1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>25|
||4.1.1.|El modelo Usuario–Tarea–Contexto<br>. . . . . . . . . . . . . . . . . .|. . .<br>25|
||4.1.2.|Atributos de calidad en uso . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>25|
|4.2.|Parte|2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>25|
|**5. Ma**|**peo de **|**Características de Calidad**|**28**|
|5.1.|Parte|1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>28|
||5.1.1.|¿Por qué priorizar? . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>28|
||5.1.2.|Matriz de priorización . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>28|
|5.2.|Parte|2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>28|



3 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

4 

|**6. Diseño de Métricas**|**31**|
|---|---|
|6.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>31|
|6.1.1.<br>Anatomía de una métrica ISO/IEC 25022 . . . . . . . . . . . . . .|. . . .<br>31|
|6.1.2.<br>Catálogo de métricas ISO/IEC 25022 aplicadas a MediSalud<br>. . .|. . . .<br>32|
|6.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>32|
|**7. Obtención de Datos**|**35**|
|7.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>35|
|7.1.1.<br>Fuentes típicas de datos para Calidad en Uso . . . . . . . . . . . .|. . . .<br>35|
|7.1.2.<br>Calidad del dato antes que calidad del indicador<br>. . . . . . . . . .|. . . .<br>35|
|7.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>35|
|**8. Automatización de la Medición**|**39**|
|8.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>39|
|8.1.1.<br>¿Por qué automatizar? . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>39|
|8.1.2.<br>Arquitectura del pipeline de medición<br>. . . . . . . . . . . . . . . .|. . . .<br>39|
|8.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>39|
|**9. Construcción de Indicadores**|**45**|
|9.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>45|
|9.1.1.<br>De la métrica al indicador . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>45|
|9.1.2.<br>Principios de buena visualización de indicadores de calidad<br>. . . .|. . . .<br>45|
|9.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>45|
|**10.Interpretación de Resultados**|**49**|
|10.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>49|
|10.1.1. Errores comunes de interpretación<br>. . . . . . . . . . . . . . . . . .|. . . .<br>49|
|10.1.2. Técnica de análisis de causa raíz (5 Por Qué) . . . . . . . . . . . .|. . . .<br>49|
|10.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>49|
|**11.Presentación Ejecutiva para Directivos**|**52**|
|11.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>52|
|11.1.1. Comunicar calidad de software a audiencias no técnicas<br>. . . . . .|. . . .<br>52|
|11.1.2. Estructura recomendada de un informe ejecutivo . . . . . . . . . .|. . . .<br>52|
|11.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>52|
|**12.Plan de Mejora Continua**|**55**|
|12.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>55|
|12.1.1. El ciclo PDCA aplicado a la Calidad en Uso. . . . . . . . . . . . .|. . . .<br>55|
|12.1.2. Gobernanza del programa . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>55|
|12.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>55|
|**Reto Final Integrador**|**58**|
|**Solución Propuesta del Reto Final**|**60**|



ÍNDICE GENERAL 

5 

|**Rúbrica de Evaluación**|**62**|
|---|---|
|**Glosario**|**65**|
|**Anexos**|**66**|



# **Índice de figuras** 

|1.|Arquitectura simplifcada de MediSalud HIS . . . . . . . . . . . . . . . .|. . . . .<br>12|
|---|---|---|
|3.1.|Ubicación de ISO/IEC 25022 dentro de la familia SQuaRE<br>. . . . . . .|. . . . .<br>23|
|8.1.|Pipeline de automatización de la medición de Calidad en Uso . . . . . .|. . . . .<br>39|



6 

# **Índice de tablas** 

|1.|Mapa general de escenarios del taller . . . . . . . . . . . . . . . . . . .|. . . . . .<br>9|
|---|---|---|
|2.|Perfles de usuario de MediSalud HIS . . . . . . . . . . . . . . . . . . .|. . . . . .<br>11|
|3.|Requerimientos no funcionales priorizados . . . . . . . . . . . . . . . .|. . . . . .<br>13|
|1.1.|Matriz de análisis inicial del caso MediSalud . . . . . . . . . . . . . . .|. . . . . .<br>17|
|2.1.|Características de Calidad en Uso según ISO/IEC 25022 . . . . . . . .|. . . . . .<br>19|
|2.2.|Plantilla de clasifcación de incidentes según ISO/IEC 25022 . . . . . .|. . . . . .<br>20|
|3.1.|Divisiones de la familia ISO/IEC 25000 (SQuaRE) . . . . . . . . . . .|. . . . . .<br>22|
|3.2.|Los tres niveles de calidad aplicados a MediSalud HIS<br>. . . . . . . . .|. . . . . .<br>24|
|4.1.|Plantilla Usuario–Tarea–Contexto<br>. . . . . . . . . . . . . . . . . . . .|. . . . . .<br>26|
|5.1.|Matriz de mapeo tarea–característica–prioridad (fragmento) . . . . . .|. . . . . .<br>29|
|6.1.|Catálogo de métricas de Calidad en Uso — MediSalud HIS<br>. . . . . .|. . . . . .<br>32|
|7.1.|Fuentes de datos según característica ISO/IEC 25022 . . . . . . . . . .|. . . . . .<br>35|
|12.1.|Cronograma propuesto del programa de medición continua. . . . . . .|. . . . . .<br>56|
|12.2.|Matriz de responsables del programa de medición . . . . . . . . . . . .|. . . . . .<br>56|
|12.3.|Solución: fcha Usuario–Tarea–Contexto de Telemedicina 2.0 . . . . . .|. . . . . .<br>60|
|12.4.|Solución: catálogo de métricas de Telemedicina 2.0 . . . . . . . . . . .|. . . . . .<br>60|
|12.5.|Rúbrica de evaluación del Reto Final Integrador<br>. . . . . . . . . . . .|. . . . . .<br>63|
|12.6.|Comandos frecuentes utilizados a lo largo del taller . . . . . . . . . . .|. . . . . .<br>66|



7 

# **Presentación General del Taller** 

## **Objetivo General** 

Desarrollar en los estudiantes la capacidad de **aplicar la norma ISO/IEC 25022** para medir la _Calidad en Uso_ de un sistema software empresarial real, combinando fundamento teórico riguroso con práctica intensiva sobre herramientas modernas de medición, automatización y visualización de indicadores de calidad. 

## **Filosofía del Taller** 

Este material **no es un compendio teórico** . Cada uno de los doce escenarios que lo componen combina una base conceptual sólida con actividades de laboratorio completamente guiadas, ejecutadas sobre un caso de estudio empresarial único y coherente: la red hospitalaria **MediSalud Ecuador** y su sistema de Hospital Information System (HIS). El estudiante recorrerá el ciclo completo de este proyecto real de evaluación de calidad en uso: desde la comprensión de la norma hasta la entrega de un informe ejecutivo y un plan de mejora continua. 

Todas las herramientas utilizadas en este taller forman parte de una edición _Community_ , _Free_ o _Trial_ suficiente para fines académicos. No se requiere presupuesto institucional o personal para su ejecución completa. 

## **Estructura de cada Escenario** 

Cada escenario sigue la misma arquitectura pedagógica: 

**1. Parte 1 — Fundamento Teórico** : definiciones, marco normativo, fórmulas y ejemplos aplicados al caso MediSalud. 

**2. Parte 2 — Actividad Práctica** : laboratorio guiado con ficha técnica, instalación, configuración, ejecución, capturas sugeridas y solución de errores. 

**3. Resultados obtenidos e interpretación.** 

#### **4. Análisis crítico.** 

**5. Preguntas de discusión.** 

**6. Conclusiones parciales.** 

8 

Presentación General 

9 

## **Mapa de Escenarios** 

Tabla 1: Mapa general de escenarios del taller 

|**#**|**Escenario**|**Duración**|
|---|---|---|
|1|Introducción al caso empresarial MediSalud<br>|2h|
|2|Comprensión de ISO/IEC 25022|3h|
|3|Comprensión del modelo SQuaRE (ISO/IEC 25000)|2h|
|4|Identifcación de atributos de Calidad en Uso|3h|
|5|Mapeo de características de calidad|2h|
|6|Diseño de métricas|3h|
|7|Obtención de datos (logs, BD, encuestas)|3h|
|8|Automatización de la medición con Python|4h|
|9|Construcción de indicadores (KPI)|3h|
|10|Interpretación de resultados|3h|
|11|Presentación ejecutiva para directivos|3h|
|12|Plan de mejora continua|2h|
||**Reto Final Integrador**|4h|



# **Caso de Estudio: Red Hospitalaria MediSalud Ecuador** 

## **Descripción de la Empresa** 

**MediSalud Ecuador** es una red privada de salud constituida en 2009, con cobertura en cinco ciudades del país (Quito, Guayaquil, Cuenca, Ambato y Manta). La red opera actualmente: 

- 4 hospitales generales de tercer nivel. 

- 12 centros de atención ambulatoria. 

- 1 laboratorio clínico centralizado con sucursales. 

- 1 central de imagenología y diagnóstico por imágenes. 

- Un servicio de telemedicina en expansión desde 2022. 

La organización atiende aproximadamente **38.000 pacientes activos por mes** y emplea a más de 2.100 colaboradores, entre personal médico, administrativo y de TI. 

## **Estructura Organizacional** 

- **Dirección General** — define objetivos estratégicos de la red. 

- **Dirección Médica** — supervisa protocolos clínicos y calidad asistencial. 

- **Gerencia de Tecnología (TI)** — responsable del sistema HIS, infraestructura y ciberseguridad. 

- **Gerencia de Calidad y Aseguramiento** — responsable de certificaciones (ISO 9001, acreditación hospitalaria) y ahora del programa de _Calidad en Uso del Software_ . 

**Departamento de Admisión y Facturación.** 

**Departamento de Enfermería y Hospitalización.** 

**Departamento de Farmacia.** 

**Call Center y Agendamiento de Citas.** 

10 

Caso de Estudio 

11 

## **El Sistema: MediSalud HIS** 

El núcleo tecnológico de la operación es **MediSalud HIS** , un sistema de información hospitalaria que integra: 

- Módulo de Historia Clínica Electrónica (HCE) (historia clínica electrónica). 

- Módulo de admisión, agendamiento y facturación. 

- Módulo de farmacia e inventario de insumos médicos. 

- Portal del paciente (web y app móvil) para citas y resultados. 

- Módulo de telemedicina (videoconsulta e indicaciones remotas). 

Módulo de reportes gerenciales y business intelligence. 

### **Usuarios del Sistema** 

Tabla 2: de usuario de MediSalud HIS 

|**Perfl**|**Uso principal**|**Usuarios activos**|
|---|---|---|
|Médico tratante|Registro de HCE, órdenes, recetas|640|
|Enfermería|Signos vitales, administración de medicamentos|910|
|Personal de admisión|Agendamiento, facturación|210|
|Farmacia|Dispensación, inventario|85|
|Paciente (portal/app)|Citas, resultados, telemedicina|38.000+|
|Gerencia / Calidad|Reportes, indicadores|45|



### **Arquitectura del Sistema** 

MediSalud HIS sigue una arquitectura de microservicios desplegada en contenedores, con las siguientes capas: 

- **Frontend web** : React, desplegado como SPA. 

- **Aplicación móvil** : Android/iOS (Flutter). 

- **Backend** : microservicios en Spring Boot y FastAPI, expuestos vía API REST. 

- **Base de datos transaccional** : PostgreSQL (HCE, facturación) y SQL Server (módulo financiero heredado). 

- **Mensajería** : colas asíncronas para integración entre laboratorio, imagenología y HCE. 

- **Infraestructura** : contenedores Docker orquestados en un clúster on-premise, con planes de migración a la nube pública. 

- **Observabilidad** : logs centralizados y métricas de infraestructura (aún incipientes, sin estandarizar). 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

12 



<!-- Start of picture text -->
Portal Web App Móvil<br>(React) (Flutter)<br>API Gateway<br>Microservicio Microservicio Microservicio<br>HCE Facturación Farmacia<br>PostgreSQL / SQL Server<br><!-- End of picture text -->

Figura 1: Arquitectura simplificada de MediSalud HIS 

### **Tecnologías Utilizadas** 

React, Flutter, Spring Boot, FastAPI, PostgreSQL, SQL Server, Docker, Nginx, RabbitMQ, Git/GitHub, Jenkins (en migración a GitHub Actions). 

## **Procesos Críticos del Negocio** 

1. Agendamiento y admisión de pacientes. 

2. Atención médica y registro de historia clínica. 

3. Prescripción y dispensación de medicamentos. 

4. Facturación y gestión de seguros/reaseguros. 

5. Telemedicina y seguimiento remoto. 

6. Generación de reportes gerenciales para toma de decisiones. 

## **Problemática Actual** 

Durante el último año, la Gerencia de Calidad ha recibido señales de alerta consistentes: 

- Quejas recurrentes de médicos por **lentitud del módulo de HCE** en horas pico (10:00– 12:00). 

- Incremento del **tiempo de espera para agendar citas** vía portal del paciente. 

- Errores de **doble facturación** reportados por el área financiera. 

- Abandono de sesiones en la app móvil antes de completar el registro de síntomas en telemedicina. 

Caso de Estudio 

13 

- Ausencia de métricas objetivas: las decisiones se toman actualmente por percepción, no por datos. 

- El área de TI afirma que «el sistema funciona correctamente» basándose únicamente en la disponibilidad de los servidores (uptime), sin considerar la experiencia real del usuario 

## **Riesgos Identificados** 

Riesgo clínico: demoras en el registro de HCE pueden retrasar decisiones médicas críticas. 

- Riesgo financiero: errores de facturación afectan el flujo de caja y la relación con aseguradoras. 

- Riesgo reputacional: fricciones en el portal del paciente afectan la retención de usuarios frente a competidores. 

Riesgo regulatorio: la normativa ecuatoriana de protección de datos en salud exige trazabilidad y disponibilidad de la información clínica. 

## **Objetivos del Negocio** 

1. Reducir en un 30 % el tiempo de registro de HCE en consulta externa en un plazo de 6 meses. 

2. Disminuir los errores de facturación duplicada a menos del 1 % de las transacciones. 

3. Aumentar la tasa de finalización de teleconsultas al 95 %. 

4. Establecer un **programa permanente de medición de Calidad en Uso** basado en ISO/IEC 25022, con reportes trimestrales a Dirección General. 

## **Requerimientos No Funcionales Relevantes para el Taller** 

Tabla 3: Requerimientos no funcionales priorizados 

|**Código**|**Requerimiento**|
|---|---|
|RNF-01|El registro de una nota de evolución clínica no debe tardar más de 8 segundos en el<br>90 % de los casos.|
|RNF-02|El portal de citas debe permitir agendar una cita en máximo 3 pasos, sin errores de<br>disponibilidad.|
|RNF-03|La tasa de errores de facturación no debe superar el 1 % de las transacciones men-<br>suales.|
|RNF-04|El sistema debe permitir auditar el uso por rol, sede y horario.|
|RNF-05|Las teleconsultas deben completarse sin caídas de conexión en más del 95 % de los<br>casos.|



_Taller ISO/IEC 25022 — Calidad en Uso_ 

14 

Este caso de estudio será utilizado de forma **transversal** en los doce escenarios del taller. Todos los archivos de datos (CSV, logs, JSON) referenciados en las prácticas simulan –de forma anonimizada y ficticia– el comportamiento real de MediSalud HIS. 

**ESCENARIO 1** 

# **Introducción al Caso Empresarial** 

Familiarizarse con el caso de estudio de la organización MediSalud Ecuador, su sistema HIS, su problemática de calidad y el rol que jugará el equipo de Aseguramiento de la Calidad del Software a lo largo del taller, estableciendo el contrato pedagógico y el entorno de trabajo compartido. 

## **— 1.1 Parte 1 Fundamento Teórico** 

### **1.1.1 El rol del Ingeniero de Calidad en un contexto empresarial real** 

En la industria, el aseguramiento de la calidad no se limita a probar que el software «no falla»; consiste en demostrar, con evidencia medible, que el sistema **permite a los usuarios reales alcanzar sus objetivos** de forma efectiva, eficiente y satisfactoria, dentro de un contexto de uso determinado. Esta idea es precisamente el núcleo de la _Calidad en Uso_ ( _Quality in Use_ ), el concepto central que se desarrollará durante todo el taller. 

### **1.1.2 De la percepción a la evidencia** 

Como se describió en el caso de estudio (capítulo introductorio), MediSalud Ecuador toma decisiones de TI basándose en percepciones («el sistema funciona bien porque los servidores están arriba»). El objetivo de este taller es transformar esa cultura hacia una **cultura de decisiones basada en métricas** , siguiendo el ciclo: 

_Observar el uso real → Medir con métricas normalizadas → Construir indicadores → Interpretar → Actuar_ 

### **1.1.3 Presentación del equipo de trabajo** 

Durante el taller, grupo de 4–5 estudiantes asumirá el rol de un **consultor externo de Calidad de Software** contratado por la Gerencia de Calidad de MediSalud para implementar, de principio a fin, un programa de medición basado en ISO/IEC 25022. 

15 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

16 

## **— 1.2 Parte 2 Actividad Práctica** 

|**Ficha de Laboratorio**<br>**Objetivo:**|Confgurar el entorno de trabajo compartido del taller<br>y realizar el primer reconocimiento del caso|
|---|---|
|**Tiempo estimado:**|± 1 hora|
|**Nivel de difcultad:**|Básico|
|**Herramientas requeridas:**|Cuenta de GitHub, Visual Studio Code, Python 3.11+,<br>Git|
|**Archivos / datos necesarios:**|Repositorio medisalud-calidad-uso (se crea en este<br>laboratorio), documento de caso de estudio (capítulo<br>previo)|



### **1.2.1 Paso 1: Creación del repositorio de trabajo** 

1. Ingresar a https://github.com y crear una cuenta institucional (si no se dispone de una). 

2. Crear un nuevo repositorio llamado medisalud-calidad-uso, público o privado según la política del curso. 

3. Clonar el repositorio en el equipo local: 

1 <mark>git clone https://github.com/<usuario>/medisalud-calidad-uso.git</mark> 2 <mark>cd medisalud-calidad-uso</mark> 3 <mark>mkdir -p data scripts dashboards docs reportes</mark> 

Listing 1.1: Clonado del repositorio de trabajo 

### **1.2.2 Paso 2: Instalación del entorno Python** 

1 <mark>python3 --version</mark> _<mark># Verificar Python 3.11 o superior</mark>_ 2 <mark>python3 -m venv venv</mark> 3 <mark>source venv/bin/activate</mark> _<mark># En Windows: venv\Scripts\activate</mark>_ 4 <mark>pip install --upgrade pip</mark> 5 <mark>pip install pandas numpy matplotlib plotly jupyter openpyxl</mark> 

Listing 1.2: Creación de entorno virtual para todo el taller 

**Error frecuente:** python3: command not found en Windows. 

**Solución:** en Windows utilizar python en lugar de python3, y verificar que la casilla «Add Python to PATH» haya sido marcada durante la instalación del intérprete descargado desde https://python.org. 

CAPÍTULO 1. INTRODUCCIÓN AL CASO EMPRESARIAL 

17 

### **1.2.3 Paso 3: Análisis dirigido del caso** 

En grupos de 4–5 estudiantes, completar la siguiente matriz en el archivo docs/analisis_inicial.md: 

Tabla 1.1: Matriz de análisis inicial del caso MediSalud 

**Pregunta guía Respuesta del grupo** ¿Cuáles son los 3 procesos más críticos del negocio? ¿Qué usuarios se ven más afectados por la problemática actual? ¿Qué evidencia tiene hoy MediSalud sobre la calidad de su software? ¿Qué evidencia le falta? 

Al finalizar este escenario, cada grupo dispone de: (1) un repositorio Git funcional con la estructura de carpetas del taller, (2) un entorno Python operativo, y (3) un documento inicial de análisis del caso que evidencia comprensión crítica de la problemática empresarial. 

### **Resolución de Problemas** 

- **Error de permisos en Git** (Permission denied (publickey)): configurar una llave SSH con ssh-keygen -t ed25519 y agregarla en GitHub _→_ Settings _→_ SSH Keys. 

- **Conflictos de versión de Python** : usar pyenv para gestionar múltiples versiones si el sistema operativo trae una versión antigua preinstalada. 

### **Preguntas de Discusión** 

1. ¿Por qué la disponibilidad de servidores (uptime) no es suficiente para afirmar que un sistema tiene buena calidad en uso? 

2. ¿Qué diferencia existe entre la calidad _interna_ , la calidad _externa_ y la calidad _en uso_ de un producto software? 

3. En el caso de MediSalud, ¿qué stakeholder se beneficiaría más de un programa de medición de calidad en uso: el paciente, el médico o la gerencia? Justifique. 

### **Conclusiones Parciales** 

Este primer escenario estableció el marco de trabajo y evidenció que las decisiones de TI en MediSalud carecen de sustento medible. Los escenarios siguientes dotarán al estudiante del marco normativo (ISO/IEC 25000 y 25022) necesario para cerrar esa brecha. 

Aproveche este escenario para indagar experiencias previas de los estudiantes con sistemas lentos o poco usables (bancos, universidades, salud) y conectar esas vivencias con el concepto de Calidad en Uso antes de formalizarlo en el Escenario 2. 

**ESCENARIO 2** 

# **Comprensión de ISO/IEC 25022** 

Comprender en profundidad la norma ISO/IEC 25022 (Measurement of Quality in Use), sus cinco características, sus fórmulas de medición y su rol dentro de la familia SQuaRE, aplicándolas conceptualmente al caso MediSalud HIS. 

## **— 2.1 Parte 1 Fundamento Teórico** 

### **2.1.1 ¿Qué es ISO/IEC 25022?** 

ISO/IEC 25022 es la norma internacional, perteneciente a la familia Software product Quality Requirements and Evaluation (SQuaRE) (ISO/IEC 25000), que define un **modelo de medición de la Calidad en Uso** de un producto software. A diferencia de ISO/IEC 25010 (que define el _modelo de calidad_ , es decir, _qué_ características debe tener un producto), la norma 25022 define _cómo medir_ dichas características desde la perspectiva de quien efectivamente utiliza el sistema en un contexto real de uso. 

La Calidad en Uso no se mide sobre el código fuente ni sobre el producto en abstracto: se mide observando a **usuarios reales realizando tareas reales** en un **contexto de uso específico** . 

### **2.1.2 Las cinco características de Calidad en Uso** 

ISO/IEC 25022 organiza la Calidad en Uso en cinco características: 

18 

CAPÍTULO 2. COMPRENSIÓN DE ISO/IEC 25022 

19 

Tabla 2.1: Características de Calidad en Uso según ISO/IEC 25022 

|**Característica**|**Defnición**|
|---|---|
|**Efectividad (Efectiveness)**|Precisión y grado de completitud con que<br>los usuarios alcanzan sus objetivos especí-<br>fcos.|
|**Efciencia (Efciency)**|Recursos utilizados (tiempo, esfuerzo, per-<br>sonas) en relación con la efectividad alcan-<br>zada.|
|**Satisfacción (Satisfaction)**|Grado en que las necesidades del usuario<br>son cubiertas, generando percepciones y<br>respuestas positivas de utilidad, confanza,<br>placer y comodidad.|
|**Libertad de Riesgo (Freedom from Risk)**|Grado en que el sistema mitiga riesgos eco-<br>nómicos, de salud, de seguridad o ambien-<br>tales potenciales.|
|**Cobertura de Contexto (Context Coverage)**|Grado en que el producto puede ser utili-<br>zado con efectividad, efciencia, libertad de<br>riesgo y satisfacción tanto en los contextos<br>previstos como en otros no previstos ini-<br>cialmente.|



### **2.1.3 Aplicación conceptual al caso MediSalud** 

Un médico (usuario) intenta registrar una nota de evolución clínica (tarea) durante la consulta externa de la mañana (contexto de uso). Si logra registrarla completa y sin errores, hay **efectividad** ; si lo hace en menos de 8 segundos, hay **eficiencia** ; si termina la consulta sintiéndose cómodo con el sistema, hay **satisfacción** ; si el sistema no expone datos sensibles del paciente durante el proceso, hay **libertad de riesgo** ; y si el mismo flujo funciona igual de bien en el hospital de Quito que en el centro ambulatorio de Manta, hay **cobertura de contexto** . 

### **2.1.4 Estructura general de una métrica en ISO/IEC 25022** 

Toda métrica de Calidad en Uso se expresa mediante la fórmula general: 



donde _A_ representa el resultado observado (tareas completadas, tiempo invertido, incidentes detectados) y _B_ representa la base de referencia (tareas intentadas, tiempo total disponible, número de usuarios). El resultado _X_ se interpreta siempre en función de un **rango deseado** , definido previamente por la organización. 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

20 

## **— 2.2 Parte 2 Actividad Práctica** 

**Objetivo:** Analizar la norma ISO/IEC 25022 y clasificar problemas reales de MediSalud según sus cinco características **Tiempo estimado:** ±1 hora **Nivel de dificultad:** Básico – Intermedio **Herramientas requeridas:** Navegador web, editor de texto / Markdown, Miro o similar (opcional) **Archivos / datos necesarios:** Lista de incidentes de MediSalud HIS (data/incidentes_2025.csv, provisto en este escenario) 

### **Paso 1: Dataset de incidentes reportados** 

Crear el archivo data/incidentes_2025_iso_25022.csv con el siguiente contenido (fragmento representativo): 

1 <mark>id,fecha,modulo,descripcion,rol_usuario,sede</mark> 2 <mark>1001,2025-11-03,HCE,Nota de evolucion tarda 22s en guardarse,Medico,Quito</mark> 3 <mark>1002,2025-11-03,Portal Citas,Usuario no logra agendar tras 3 intentos,Paciente,Guayaquil</mark> 4 <mark>1003,2025-11-04,Facturacion,Factura duplicada al reintentar pago,Admision,Cuenca</mark> 5 <mark>1004,2025-11-05,Telemedicina,Videollamada se corta a los 4 minutos,Paciente,Ambato</mark> 6 <mark>1005,2025-11-05,HCE,Datos de otro paciente visibles brevemente,Medico,Quito</mark> 7 <mark>1006,2025-11-06,Portal Citas,Formulario confuso, abandono de registro,Paciente,Manta</mark> 

Listing 2.1: Fragmento de incidentes reportados en MediSalud HIS(ejemplo) 

### **Paso 2: Clasificación según las cinco características** 

En equipos, clasificar cada incidente del dataset anterior en la característica de ISO/IEC 25022 que mejor lo representa, completando la tabla: 

Tabla 2.2: Plantilla de clasificación de incidentes según ISO/IEC 25022 

|**ID**<br>**Justifcación**|**Característica**|
|---|---|
|1001||
|1002||
|1003||
|1004||
|1005||
|1006||



CAPÍTULO 2. COMPRENSIÓN DE ISO/IEC 25022 

21 

Como grupo, discutan el incidente 1005. ¿Por qué corresponde principalmente a _Libertad de Riesgo_ y no a _Efectividad_ , a pesar de tratarse también de un error del sistema? 

Cada equipo entrega una tabla de clasificación completa con justificación técnica, demostrando la capacidad de diferenciar las cinco características de la norma sobre casos reales, no solo sobre memorizadas. 

### **Resolución de Problemas** 

- **Confusión frecuente:** los estudiantes tienden a clasificar todo como «Efectividad». **Solución docente:** preguntar explícitamente «¿el usuario logró o no su objetivo?» (Efectividad) versus «¿a qué costo/riesgo lo logró?» (Eficiencia / Riesgo). 

### **Preguntas de Discusión** 

1. ¿Puede un sistema ser _efectivo_ pero no _eficiente_ ? Dé un ejemplo del caso MediSalud. 

2. ¿Por qué la _Cobertura de Contexto_ es especialmente relevante para una red hospitalaria con sedes en cinco ciudades distintas? 

### **Conclusiones Parciales** 

El estudiante ha comprendido que ISO/IEC 25022 provee un vocabulario común y estructurado para describir problemas de calidad que, en la práctica diaria de MediSalud, se reportaban de forma ambigua e inconsistente. 

**ESCENARIO 3** 

# **Comprensión del Modelo SQuaRE** 

Ubicar a ISO/IEC 25022 dentro de la familia completa ISO/IEC 25000 (SQuaRE), diferenciando claramente entre modelo de calidad, medición de calidad, requerimientos y evaluación, para que el estudiante comprenda el marco normativo completo en el que se inserta el taller. 

## **— 3.1 Parte 1 Fundamento Teórico** 

### **3.1.1 ¿Qué es SQuaRE?** 

SQuaRE es la familia de normas internacionales ISO/IEC 25000, que reemplazó y unificó a las antiguas normas ISO/IEC 9126 e ISO/IEC 14598. SQuaRE organiza el ciclo completo de gestión de la calidad del software en cinco divisiones: 

Tabla 3.1: Divisiones de la familia ISO/IEC 25000 (SQuaRE) 

|**División**|**Rango**|**Propósito**|
|---|---|---|
|Gestión de calidad|2500n|Guía de uso de toda la familia SQuaRE.|
|Modelo de calidad|2501n|Defne<br>_qué_<br>características<br>debe<br>tener<br>un<br>producto<br>(ISO/IEC 25010) y su calidad en uso.|
|Medición de calidad|2502n|Defne _cómo medir_<br>cada característica: aquí reside|
|||**ISO/IEC 25022**(Calidad en Uso), junto con 25023 (ca-|
|||lidad de producto) y 25024 (calidad de datos).|
|Requerimientos de calidad|2503n|Guía para especifcar requerimientos de calidad.|
|Evaluación de calidad|2504n|Guía para el proceso de evaluación formal de calidad.|



### **3.1.2 Relación entre ISO/IEC 25010 y 25022** 

ISO/IEC 25010 define el **modelo de calidad en uso** con sus cinco características (las mismas vistas en el Escenario 2). ISO/IEC 25022 toma exactamente esas características y les asocia **métricas concretas, fórmulas y escalas de medición** . Es decir: **25010 dice qué medir; 25022 dice cómo medirlo** . 

22 

CAPÍTULO 3. COMPRENSIÓN DEL MODELO SQUARE 

23 



<!-- Start of picture text -->
ISO/IEC 25000<br>Guía general SQuaRE<br>ISO/IEC 25010<br>Modelo de Calidad (qué medir)<br>ISO/IEC 25022<br>Medición de Calidad en Uso (cómo medir)<br>ISO/IEC 25040<br>Proceso de Evaluación<br><!-- End of picture text -->

Figura 3.1: Ubicación de ISO/IEC 25022 dentro de la familia SQuaRE 

## **— 3.2 Parte 2 Actividad Práctica** 

|**Ficha de Laboratorio**<br>**Objetivo:**|Construir un mapa conceptual de la familia SQuaRE<br>aplicado a MediSalud y diferenciar los tres niveles de<br>calidad (interna, externa, en uso)|
|---|---|
|**Tiempo estimado:**|±1 hora|
|**Nivel de difcultad:**|Básico|
|**Herramientas requeridas:**|Draw.io / Miro|
|**Archivos / datos necesarios:**|Documento resumen de las normas (proporcionado por<br>el docente o buscado por los estudiantes en fuentes<br>ofciales de ISO)|



### **Paso 1: Investigación dirigida** 

Cada grupo investiga y resume en minimo 2 páginas, en sus propias palabras, la diferencia entre: 

Calidad interna (código, arquitectura) — ISO/IEC 25010, vista estática. 

- Calidad externa (comportamiento observable en pruebas) — ISO/IEC 25010, vista dinámica en entorno controlado. 

Calidad en uso (experiencia real del usuario) — ISO/IEC 25022, vista en producción. 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

24 

### **Paso 2: Aplicación al caso MediSalud** 

Completar la tabla identificando, para cada nivel, un ejemplo concreto del sistema HIS: 

Tabla 3.2: Los tres niveles de calidad aplicados a MediSalud HIS 

|**Nivel**|**Ejemplo en MediSalud HIS**|
|---|---|
|Calidad interna|Complejidad ciclomática del módulo de facturación medida con SonarQube.|
|Calidad externa|Pruebas de carga con JMeter simulando 500 usuarios concurrentes en el portal<br>de citas.|
|Calidad en uso|Tiempo real que tarda un médico en registrar una nota clínica durante con-<br>sulta externa (dato de producción).|



Cada grupo entrega un mapa conceptual (imagen o diagrama) que ubica correctamente las normas ISO/IEC 25000, 25010, 25022 y 25040, y diferencia sin ambigüedad los tres niveles de calidad usando ejemplos propios del caso MediSalud. 

### **Preguntas de Discusión** 

1. ¿Puede un sistema tener excelente calidad interna (código limpio) y mala calidad en uso? Explique con un ejemplo. 

2. ¿Por qué SonarQube (calidad interna) no es suficiente para que MediSalud resuelva su problemática de lentitud percibida por los médicos? 

### **Conclusiones Parciales** 

El estudiante reconoce que la calidad en uso es el nivel más cercano al negocio y al paciente, y que por ello será el foco exclusivo del resto del taller, sin descuidar que se apoya en buenas prácticas de calidad interna y externa. 

**ESCENARIO 4** 

# **Identificación de Atributos de Calidad en Uso** 

Identificar, a partir de las tareas reales de los usuarios de MediSalud HIS, los atributos concretos de Calidad en Uso que deben medirse, estableciendo tareas, usuarios y contextos de uso según la estructura exigida por ISO/IEC 25022. 

## **— 4.1 Parte 1 Fundamento Teórico** 

### **4.1.1 El modelo Usuario–Tarea–Contexto** 

ISO/IEC 25022 exige definir, antes de cualquier métrica, tres elementos: 

1. **Usuario primario** : quién ejecuta la tarea (rol). 

2. **Tarea representativa** : qué objetivo concreto persigue el usuario. 

3. **Contexto de uso** : en qué condiciones (dispositivo, ubicación, carga del sistema, horario) se ejecuta la tarea. 

### **4.1.2 Atributos de calidad en uso** 

Un _atributo_ es una propiedad medible derivada de una característica. Por ejemplo, de la característica _Efectividad_ se derivan atributos como «completitud de tarea» o «precisión de tarea»; de _Eficiencia_ , atributos como «tiempo de tarea» o «eficiencia de tarea humana». 

## **— 4.2 Parte 2 Actividad Práctica** 

25 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

26 

**Objetivo:** Definir tareas representativas de usuario y sus atributos de calidad en uso para tres procesos críticos de MediSalud **Tiempo estimado:** 3 horas **Nivel de dificultad:** Intermedio **Herramientas requeridas:** Editor de hojas de cálculo o Markdown **Archivos / datos necesarios:** Procesos críticos identificados en el capítulo de caso de estudio 

### **Paso 1: Selección de procesos** 

Cada grupo selecciona 3 de los 6 procesos críticos de MediSalud (Escenario introductorio) y define, para cada uno, una tarea representativa siguiendo la plantilla: 

Tabla 4.1: Plantilla Usuario–Tarea–Contexto 

**Campo Ejemplo completado** Proceso Atención médica y registro de HCE Usuario primario Médico tratante Tarea representativa Registrar una nota de evolución clínica completa de un paciente Contexto de uso Consulta externa, horario 10:00–12:00, red interna del hospital de Quito, carga alta de usuarios concurrentes Atributos de Calidad en Uso relevantes Tiempo de tarea (Eficiencia), completitud de la nota (Efectividad), percepción de fluidez (Satisfacción) 

Repitan la plantilla anterior para _Agendamiento de citas por el paciente_ y para _Facturación de una consulta con seguro médico_ . 

Insista en que el contexto de uso no es un detalle decorativo: variables como «hora pico» 

o «sede» explican después por qué la misma métrica puede arrojar valores muy distintos entre Quito y Manta. 

Cada grupo entrega tres fichas Usuario–Tarea–Contexto completas y coherentes con el caso MediSalud, listas para ser convertidas en métricas concretas en el Escenario 6. 

CAPÍTULO 4. IDENTIFICACIÓN DE ATRIBUTOS DE CALIDAD EN USO 

27 

### **Preguntas de Discusión** 

1. ¿Por qué es incorrecto definir una tarea como «usar el sistema HIS» en lugar de «registrar una nota de evolución clínica»? 

2. ¿Qué ocurre si se mide la eficiencia sin haber definido el contexto de uso (por ejemplo, sin diferenciar hora pico de hora valle)? 

### **Conclusiones Parciales** 

El estudiante ha aprendido a operacionalizar procesos de negocio abstractos en tareas medibles, usuarios concretos y contextos de uso explícitos, requisito indispensable antes de diseñar cualquier métrica ISO/IEC 25022. 

**ESCENARIO 5** 

# **Mapeo de Características de Calidad** 

Construir la matriz de mapeo que vincula cada tarea Usuario–Tarea–Contexto definida en el Escenario 4 con las cinco características de ISO/IEC 25022, priorizando cuáles serán medidas en el programa de MediSalud. 

## **— 5.1 Parte 1 Fundamento Teórico** 

### **5.1.1 ¿Por qué priorizar?** 

Medir las cinco características para todas las tareas posibles no es viable ni deseable: consume recursos y genera ruido. La práctica profesional recomienda priorizar según **impacto en el negocio** y **riesgo** , criterios ya identificados en el caso de estudio. 

### **5.1.2 Matriz de priorización** 

Se recomienda una matriz de doble entrada: _Impacto en el negocio_ (alto/medio/bajo) frente a _Frecuencia de la tarea_ (alta/media/baja), seleccionando para medición prioritaria las combinaciones alto–alto y alto–medio. 

## **— 5.2 Parte 2 Actividad Práctica** 

|**Ficha de Laboratorio**<br>**Objetivo:**|Elaborar la matriz de mapeo tarea–característica–<br>prioridad para el programa de medición de MediSalud|
|---|---|
|**Tiempo estimado:**|2 horas|
|**Nivel de difcultad:**|Intermedio|
|**Herramientas requeridas:**|Hoja de cálculo (Excel/Google Sheets)|
|**Archivos / datos necesarios:**|Fichas Usuario–Tarea–Contexto del Escenario 4|



28 

CAPÍTULO 5. MAPEO DE CARACTERÍSTICAS DE CALIDAD 

29 

### **Paso 1: Construcción de la matriz** 

Tabla 5.1: Matriz de mapeo tarea–característica–prioridad (fragmento) 

|**Tarea**|**Impacto**|**Frecuencia**|**Característica(s)**<br>**ISO**<br>**25022**<br>**Prioridad**|
|---|---|---|---|
|Registrar nota de evolución clínica|Alto|Alta|Efciencia,<br>Efec-<br>tivi-<br>**1**|
||||dad|
|Agendar cita en portal|Alto|Alta|Efectividad,<br>Sa-<br>**1**|
||||tis-|
||||fac-|
||||ción|
|Facturar consulta con seguro|Alto|Media|Libertad<br>de<br>**2**|
||||Ries-|
||||go,|
||||Efec-|
||||tivi-|
||||dad|
|Completar teleconsulta|Medio|Media|Efectividad,<br>Co-<br>**2**|
||||ber-|
||||tura|
||||de|
||||Con-|
||||tex-|
||||to|
|Consultar historial de resultados de laboratorio|Bajo|Alta|Satisfacción 3|



El equipo entrega una matriz priorizada con al menos 6 tareas, sirviendo como insumo directo para el diseño de métricas del Escenario 6, donde solo se desarrollarán en profundidad las tareas de prioridad 1 y 2. 

### **Preguntas de Discusión** 

1. ¿Qué riesgo corre una organización que intenta medir absolutamente todo desde el primer día de un programa de calidad en uso? 

2. ¿Por qué «Consultar historial de resultados» tiene menor prioridad pese a tener alta frecuencia? 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

30 

### **Conclusiones Parciales** 

El estudiante comprende que un programa de medición sostenible se construye de forma incremental, comenzando por las tareas de mayor impacto y frecuencia, principio que también rige la implementación de sistemas de monitoreo en la industria (por ejemplo, en observabilidad de software). 

**ESCENARIO 6** 

# **Diseño de Métricas** 

Diseñar formalmente, siguiendo la estructura de ISO/IEC 25022, las métricas de Calidad en Uso para las tareas priorizadas de MediSalud: fórmula, variables, unidad, rango deseado e interpretación. 

## **— 6.1 Parte 1 Fundamento Teórico** 

### **6.1.1 Anatomía de una métrica ISO/IEC 25022** 

Toda métrica formal debe documentar: 

**Nombre de la métrica.** 

**Característica asociada.** 

**Propósito de la medición.** 

**Fórmula** ( _X_ = _A/B_ u otra estructura). 

**de variables.** 

**Unidad de medida.** 

**Rango deseado / umbral.** 

**Fuente de datos.** 

**Interpretación.** 

31 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

32 

### **6.1.2 Catálogo de métricas ISO/IEC 25022 aplicadas a MediSalud** 

Tabla 6.1: Catálogo de métricas de Calidad en Uso — MediSalud HIS 

|**Característica**|**Métrica**|**Fórmula**|
|---|---|---|
|Efectividad|Completitud de tarea (registro de<br>HCE)|_X_<br>=<br>Notas completadas correctamente<br>|
|Efectividad|Tasadeéxitodeaendamiento|Notas intentadas<br>_X_= <sup>Citas agendadas con éxito</sup>|
|Efciencia|g<br>Tiempo de tarea (registro clínico)|<br>Intentos de agendamiento<br>_X_ =<br>�Tiempo por nota<br>Número de notas<br>Eftiidd|
|Efciencia<br>Satisfacción<br>Libertad de Riesgo<br>|Efciencia relativa del usuario<br>Índice de satisfacción (encuesta)<br>Tasa de errores de facturación<br>|_X_ =<br>ecva<br>Tiempo invertido<br>_X_ =<br>�Puntajes de satisfacción<br>N. de encuestados<br>_X_ = <sup>Facturas erróneas</sup><br>Facturas emitidas|
|Cobertura de Contexto|Consistencia entre sedes|_X_<br>=<br>1<br>_−_<br>_|_Métrica sede A_−_Métrica sede B_|_|
|||Métrica sede A|



#### **Métrica: Tiempo de tarea — registro de nota clínica.** 

> <u>�</u> _ti_ **Fórmula:** _X_ =<sup>donde</sup><sup>_ti_eseltiempo(segundos)quetardaelregistro</sup><sup>_i_-ésimoy</sup><sup>_n_</sup> _n_<sup>,</sup> el número total de registros observados. 

**Rango deseado:** _X ≤_ 8 segundos (según RNF-01 del caso de estudio). 

**Fuente de datos:** logs de la aplicación web/HIS (marca de tiempo al abrir el formulario y al confirmar el guardado). 

**Interpretación:** valores por encima de 8 segundos de forma sostenida indican fricción de usabilidad o degradación de desempeño técnico, ambos con impacto directo en la atención médica. 

## **— 6.2 Parte 2 Actividad Práctica** 

|**Ficha de Laboratorio**<br>**Objetivo:**|Documentar formalmente 5 métricas ISO/IEC 25022<br>(una por característica) usando la fcha estándar de<br>diseño de métrica|
|---|---|
|**Tiempo estimado:**|3 horas|
|**Nivel de difcultad:**|Intermedio – Avanzado|
|**Herramientas requeridas:**|Plantilla de fcha de métrica (Markdown/Excel)|
|**Archivos / datos necesarios:**|Matriz priorizada del Escenario 5|



CAPÍTULO 6. DISEÑO DE MÉTRICAS 

33 

### **Paso 1: Ficha estándar de métrica** 

Cada grupo documenta, para cada una de las 5 características, una métrica siguiendo esta 

**Nombre: Característica: Propósito: Fórmula: Variables: Unidad: Rango deseado: Fuente de datos: Frecuencia de medición: Responsable:** 

**Error frecuente:** definir una fórmula sin especificar la unidad de las variables (por ejemplo, no aclarar si el tiempo se mide en segundos o minutos). Esto genera indicadores incomparables entre sedes o entre sprints de medición. **Solución:** exigir siempre la unidad explícita en la ficha. 

Cada equipo entrega un catálogo de al menos 5 métricas formalmente documentadas, listas para ser calculadas automáticamente en los Escenarios 7 y 8 con datos reales (simulados) de MediSalud. 

### **Resolución de Problemas** 

- **Métrica ambigua:** si dos estudiantes del mismo grupo calculan manualmente la métrica y obtienen resultados distintos, la fórmula o las variables no están suficientemente especificadas; se debe revisar la ficha. 

### **Preguntas de Discusión** 

1. ¿Por qué es importante fijar de antemano el _rango deseado_ y no solo calcular el valor de la métrica? 

2. ¿Qué diferencia existe entre una métrica de _Eficiencia_ y un simple cronómetro de tiempo de respuesta del servidor? 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

34 

### **Conclusiones Parciales** 

El estudiante ha traducido conceptos normativos abstractos en métricas formales, reproducibles y accionables, sentando las bases técnicas para la automatización que se abordará en los siguientes escenarios. 

**ESCENARIO 7** 

# **Obtención de Datos** 

Identificar y generar las fuentes de datos necesarias (logs de aplicación, base de datos, encuestas de satisfacción) para calcular las métricas diseñadas en el Escenario 6, preparando los archivos que se automatizarán en el Escenario 8. 

## **— 7.1 Parte 1 Fundamento Teórico** 

### **7.1.1 Fuentes típicas de datos para Calidad en Uso** 

Tabla 7.1: Fuentes de datos según característica ISO/IEC 25022 

|**Característica**|**Fuente típica de datos**|
|---|---|
|Efectividad|Logs de aplicación (eventos de éxito/fracaso de tarea), base de datos<br>transaccional.|
|Efciencia|Logs con marcas de tiempo (_timestamps_), trazas de _Application Per-_<br>_formance Monitoring_.|
|Satisfacción|Encuestas (SUS, CSAT, NPS), comentarios de soporte técnico.|
|Libertad de Riesgo|Registros de incidentes, logs de errores, auditorías de seguridad.|
|Cobertura de Contexto|Metadatos de sesión: sede, dispositivo, horario, tipo de red.|



### **7.1.2 Calidad del dato antes que calidad del indicador** 

Un indicador construido sobre datos incompletos, duplicados o mal etiquetados produce conclusiones erróneas, sin importar cuán correcta sea la fórmula ISO/IEC 25022 aplicada. Por ello, este escenario dedica tiempo explícito a la **limpieza y validación de datos** antes de automatizar nada. 

## **— 7.2 Parte 2 Actividad Práctica** 

35 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

36 

**Objetivo:** Generar y validar los conjuntos de datos base (logs de HCE, encuestas de satisfacción, incidentes de facturación) que alimentarán el cálculo automatizado de métricas **Tiempo estimado:** 3 horas **Nivel de dificultad:** Intermedio **Herramientas requeridas:** Python 3.11+, Jupyter Notebook, Pandas, DBeaver (opcional), PostgreSQL o SQLite **Archivos / datos necesarios:** Scripts generadores provistos en este escenario 

### **Paso 1: Generación del log simulado de registro de HCE** 

Crear el archivo scripts/generar_logs_hce.py: 

1 <mark>"""</mark> 2 <mark>Genera un log sintetico de eventos de registro de notas de evolucion clinica</mark> 3 <mark>en el modulo HCE de MediSalud HIS, simulando 5 dias habiles y 5 sedes.</mark> 4 <mark>"""</mark> 5 **<mark>import</mark>** <mark>csv</mark> 6 **<mark>import</mark>** <mark>random</mark> 7 **<mark>from</mark>** <mark>datetime</mark> **<mark>import</mark>** <mark>datetime, timedelta</mark> 8 9 <mark>random.seed(42)</mark> 10 11 <mark>SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]</mark> 12 <mark>MEDICOS_POR_SEDE = 12</mark> 13 <mark>FECHA_INICIO = datetime(2025, 11, 3, 7, 0, 0)</mark> 14 <mark>DIAS = 5</mark> 15 16 <mark>filas = []</mark> 17 <mark>evento_id = 1</mark> 18 19 **<mark>for</mark>** <mark>dia</mark> **<mark>in range</mark>** <mark>(DIAS):</mark> 20 <mark>fecha_dia = FECHA_INICIO + timedelta(days=dia)</mark> 21 **<mark>for</mark>** <mark>sede</mark> **<mark>in</mark>** <mark>SEDES:</mark> 22 _<mark># Mayor carga en Quito y Guayaquil (hospitales mas grandes)</mark>_ 23 <mark>n_eventos = 180</mark> **<mark>if</mark>** <mark>sede</mark> **<mark>in</mark>** <mark>("Quito", "Guayaquil")</mark> **<mark>else</mark>** <mark>90</mark> 24 **<mark>for</mark>** <mark>_</mark> **<mark>in range</mark>** <mark>(n_eventos):</mark> 25 <mark>hora = random.randint(7, 18)</mark> 26 <mark>minuto = random.randint(0, 59)</mark> 27 <mark>timestamp = fecha_dia.replace(hour=hora, minute=minuto)</mark> 28 29 _<mark># Simulamos que en horas pico (10-12h) el tiempo de registro sube</mark>_ 30 <mark>es_hora_pico = 10 <= hora <= 12</mark> 31 <mark>tiempo_base = random.gauss(6.5, 1.5)</mark> 32 **<mark>if</mark>** <mark>es_hora_pico:</mark> 33 <mark>tiempo_base += random.gauss(4.0, 2.0)</mark> _<mark># degradacion en pico</mark>_ 34 <mark>tiempo_segundos =</mark> **<mark>max</mark>** <mark>(1.5,</mark> **<mark>round</mark>** <mark>(tiempo_base, 2))</mark> 

CAPÍTULO 7. OBTENCIÓN DE DATOS 

37 

35 36 _<mark># 96 % de las notas se completan correctamente</mark>_ 37 <mark>completada = random.random() < 0.96</mark> 38 39 <mark>medico_id = f"MED-{sede[:3].upper()}-{random.randint(1, MEDICOS_POR_SEDE):02d}"</mark> 40 41 <mark>filas.append({</mark> 42 <mark>"evento_id": evento_id,</mark> 43 <mark>"timestamp": timestamp.isoformat(),</mark> 44 <mark>"sede": sede,</mark> 45 <mark>"medico_id": medico_id,</mark> 46 <mark>"tiempo_segundos": tiempo_segundos,</mark> 47 <mark>"completada":</mark> **<mark>int</mark>** <mark>(completada),</mark> 48 <mark>})</mark> 49 <mark>evento_id += 1</mark> 50 51 **<mark>with open</mark>** <mark>("data/logs_hce.csv", "w", newline="", encoding="utf-8")</mark> **<mark>as</mark>** <mark>f:</mark> 52 <mark>writer = csv.DictWriter(f, fieldnames=filas[0].keys())</mark> 53 <mark>writer.writeheader()</mark> 54 <mark>writer.writerows(filas)</mark> 55 56 **<mark>print</mark>** <mark>(f"Se generaron {len(filas)} eventos en data/logs_hce.csv")</mark> 

Listing 7.1: Generador de logs sintéticos de registro de HCE 

Ejecutar: 

1 <mark>python3 scripts/generar_logs_hce.py</mark> 2 <mark>head -5 data/logs_hce.csv</mark> 

Listing 7.2: Ejecución del generador de logs 

### **Paso 2: Generación de encuesta de satisfacción (CSAT)** 

Crear data/encuesta_satisfaccion.csv con columnas respuesta_id, sede, rol, puntaje_csat (1-5), comentario. El docente puede proveer un dataset de 150 respuestas simuladas (disponible como material complementario del taller) o generarlo con un script análogo al anterior. 

### **Paso 3: Validación de datos con Pandas** 

En Jupyter Notebook (scripts/01_validacion_datos.ipynb): 

1 **<mark>import</mark>** <mark>pandas</mark> **<mark>as</mark>** <mark>pd</mark> 2 3 <mark>df = pd.read_csv("data/logs_hce.csv")</mark> 4 5 _<mark># 1. Verificar valores nulos</mark>_ 6 **<mark>print</mark>** <mark>("Valores nulos por columna:")</mark> 7 **<mark>print</mark>** <mark>(df.isnull().</mark> **<mark>sum</mark>** <mark>())</mark> 8 9 _<mark># 2. Verificar rangos logicos</mark>_ 10 **<mark>print</mark>** <mark>("\nTiempos fuera de rango (negativos o mayores a 120s):")</mark> 11 **<mark>print</mark>** <mark>(df[(df["tiempo_segundos"] < 0) | (df["tiempo_segundos"] > 120)])</mark> 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

38 

12 13 _<mark># 3. Verificar duplicados</mark>_ 14 **<mark>print</mark>** <mark>("\nEventos duplicados:", df.duplicated(subset=["evento_id"]).</mark> **<mark>sum</mark>** <mark>())</mark> 15 16 _<mark># 4. Resumen descriptivo</mark>_ 17 **<mark>print</mark>** <mark>("\nResumen estadistico de tiempo_segundos:")</mark> 18 **<mark>print</mark>** <mark>(df["tiempo_segundos"].describe())</mark> 

Listing 7.3: Validación básica de calidad del dato 

**Error frecuente:** FileNotFoundError: data/logs_hce.csv. 

**Solución:** verificar que el notebook o script se ejecuta desde la raíz del repositorio (medisalud-calidad-uso/) y que la carpeta data/ existe (mkdir -p data). 

Al finalizar este escenario, el equipo dispone de al menos dos archivos CSV validados (logs_hce.csv y encuesta_satisfaccion.csv), sin nulos, sin duplicados y con rangos lógicos verificados, listos para ser procesados automáticamente. 

### **Preguntas de Discusión** 

1. ¿Qué consecuencias tendría calcular la métrica de _tiempo de tarea_ sin antes eliminar los valores atípicos ( _outliers_ ) causados por sesiones abandonadas? 

2. ¿Por qué la fuente de datos de _Satisfacción_ (encuestas) es cualitativamente distinta a la de _Eficiencia_ (logs)? ¿Qué implica esto para su frecuencia de recolección? 

### **Conclusiones Parciales** 

El estudiante reconoce que la obtención de datos confiables es un prerrequisito técnico ineludible, y ha practicado técnicas básicas de validación de datos con Pandas, herramienta que será la columna vertebral de la automatización en el Escenario 8. 

**ESCENARIO 8** 

# **Automatización de la Medición** 

Construir un pipeline en Python que calcule automáticamente las cinco métricas ISO/IEC 25022 del catálogo de MediSalud a partir de los datos validados en el Escenario 7, generando un archivo de indicadores reutilizable para los escenarios de visualización. 

## **— 8.1 Parte 1 Fundamento Teórico** 

### **8.1.1 ¿Por qué automatizar?** 

Calcular métricas manualmente en una hoja de cálculo no escala: MediSalud requiere reportes **trimestrales** y, eventualmente, **continuos** . La automatización garantiza reproducibilidad, trazabilidad y la posibilidad de integrar la medición en un pipeline de Integración Continua / Entrega Continua (CI/CD). 

### **8.1.2 Arquitectura del pipeline de medición** 

|Datos crudos<br>(CSV/logs)|Limpieza<br>Extract, Transform, Load (ETL) (Pandas)|Cálculo de<br>métricas ISO 25022|Indi<br>(JSO|
|---|---|---|---|



Figura 8.1: Pipeline de automatización de la medición de Calidad en Uso 

## **— 8.2 Parte 2 Actividad Práctica** 

39 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

40 

|**Ficha de Laboratorio**<br>**Objetivo:**|Implementar en Python un módulo que calcule las mé-<br>tricas de Efectividad, Efciencia, Satisfacción y Liber-<br>tad de Riesgo a partir de los datos generados en el<br>Escenario 7|
|---|---|
|**Tiempo estimado:**|4 horas|
|**Nivel de difcultad:**|Avanzado|
|**Herramientas requeridas:**|Python 3.11+, Pandas, NumPy, pytest (opcional para<br>pruebas unitarias)|
|**Archivos / datos necesarios:**|data/logs_hce.csv,data/encuesta_satisfaccion.csv,<br>data/incidentes_2025.csv|



### **Paso 1: Módulo de cálculo de métricas** 

Crear scripts/metricas_iso25022.py: 

1 <mark>"""</mark> 2 <mark>Modulo de calculo de metricas de Calidad en Uso (ISO/IEC 25022)</mark> 3 <mark>para el sistema MediSalud HIS.</mark> 4 5 <mark>Cada funcion retorna un diccionario con: valor, unidad, umbral y estado.</mark> 6 <mark>"""</mark> 7 **<mark>import</mark>** <mark>pandas</mark> **<mark>as</mark>** <mark>pd</mark> 8 9 10 <mark>UMBRAL_TIEMPO_TAREA = 8.0</mark> _<mark># segundos, segun RNF-01</mark>_ 11 <mark>UMBRAL_TASA_ERROR_FACT = 0.01</mark> _<mark># 1 %, segun RNF-03</mark>_ 12 <mark>UMBRAL_EFECTIVIDAD = 0.95</mark> _<mark># 95 % de completitud esperada</mark>_ 13 14 15 **<mark>def</mark>** <mark>cargar_datos():</mark> 16 <mark>"""Carga los tres datasets base del programa de medicion."""</mark> 17 <mark>logs = pd.read_csv("data/logs_hce.csv")</mark> 18 <mark>encuesta = pd.read_csv("data/encuesta_satisfaccion.csv")</mark> 19 <mark>incidentes = pd.read_csv("data/incidentes_2025.csv")</mark> 20 **<mark>return</mark>** <mark>logs, encuesta, incidentes</mark> 21 22 23 **<mark>def</mark>** <mark>metrica_efectividad(logs: pd.DataFrame) -></mark> **<mark>dict</mark>** <mark>:</mark> 24 <mark>"""</mark> 25 <mark>Efectividad = notas completadas correctamente / notas intentadas.</mark> 26 <mark>"""</mark> 27 <mark>total =</mark> **<mark>len</mark>** <mark>(logs)</mark> 28 <mark>completadas = logs["completada"].</mark> **<mark>sum</mark>** <mark>()</mark> 29 <mark>valor =</mark> **<mark>round</mark>** <mark>(completadas / total, 4)</mark> **<mark>if</mark>** <mark>total</mark> **<mark>else</mark>** <mark>0.0</mark> 30 **<mark>return</mark>** <mark>{</mark> 31 <mark>"nombre": "Completitud de registro de HCE",</mark> 32 <mark>"caracteristica": "Efectividad",</mark> 33 <mark>"valor": valor,</mark> 

CAPÍTULO 8. AUTOMATIZACIÓN DE LA MEDICIÓN 

41 

34 <mark>"unidad": "proporcion",</mark> 35 <mark>"umbral": UMBRAL_EFECTIVIDAD,</mark> 36 <mark>"cumple": valor >= UMBRAL_EFECTIVIDAD,</mark> 37 <mark>}</mark> 38 

39 

40 **<mark>def</mark>** <mark>metrica_eficiencia(logs: pd.DataFrame) -></mark> **<mark>dict</mark>** <mark>:</mark> 41 <mark>"""</mark> 42 <mark>Eficiencia = tiempo promedio de registro de nota clinica (segundos).</mark> 43 <mark>"""</mark> 44 <mark>valor =</mark> **<mark>round</mark>** <mark>(logs["tiempo_segundos"].mean(), 2)</mark> 45 **<mark>return</mark>** <mark>{</mark> 46 <mark>"nombre": "Tiempo promedio de registro de HCE",</mark> 47 <mark>"caracteristica": "Eficiencia",</mark> 48 <mark>"valor": valor,</mark> 49 <mark>"unidad": "segundos",</mark> 50 <mark>"umbral": UMBRAL_TIEMPO_TAREA,</mark> 51 <mark>"cumple": valor <= UMBRAL_TIEMPO_TAREA,</mark> 52 <mark>}</mark> 53 

54 

55 **<mark>def</mark>** <mark>metrica_eficiencia_por_sede(logs: pd.DataFrame) -> pd.DataFrame:</mark> 56 <mark>"""Desagrega el tiempo promedio de tarea por sede (Cobertura de Contexto)."""</mark> 57 **<mark>return</mark>** <mark>(</mark> 58 <mark>logs.groupby("sede")["tiempo_segundos"]</mark> 59 <mark>.mean()</mark> 60 <mark>.</mark> **<mark>round</mark>** <mark>(2)</mark> 61 <mark>.reset_index()</mark> 62 <mark>.rename(columns={"tiempo_segundos": "tiempo_promedio_segundos"})</mark> 63 <mark>)</mark> 64 

65 

66 **<mark>def</mark>** <mark>metrica_satisfaccion(encuesta: pd.DataFrame) -></mark> **<mark>dict</mark>** <mark>:</mark> 67 <mark>"""</mark> 68 <mark>Satisfaccion = promedio de puntaje CSAT (escala 1-5), normalizado a 0-1.</mark> 69 <mark>"""</mark> 70 <mark>promedio_csat = encuesta["puntaje_csat"].mean()</mark> 71 <mark>valor =</mark> **<mark>round</mark>** <mark>(promedio_csat / 5, 4)</mark> 72 **<mark>return</mark>** <mark>{</mark> 73 <mark>"nombre": "Indice de satisfaccion (CSAT normalizado)",</mark> 74 <mark>"caracteristica": "Satisfaccion",</mark> 75 <mark>"valor": valor,</mark> 76 <mark>"unidad": "proporcion (0-1)",</mark> 77 <mark>"umbral": 0.80,</mark> 78 <mark>"cumple": valor >= 0.80,</mark> 79 <mark>}</mark> 80 81 82 **<mark>def</mark>** <mark>metrica_libertad_riesgo(incidentes: pd.DataFrame, total_transacciones:</mark> **<mark>int</mark>** <mark>) -></mark> **<mark>dict</mark>** <mark>:</mark> 83 <mark>"""</mark> 84 <mark>Libertad de Riesgo = tasa de incidentes de facturacion sobre el total</mark> 85 <mark>de transacciones de facturacion procesadas en el periodo.</mark> 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

42 

|86<br>87|"""<br>incidentes_facturacion = incidentes[incidentes["modulo"] == "Facturacion"]|
|---|---|
|88|valor = **round**(**len**(incidentes_facturacion) / total_transacciones, 4)|
|89|**return** {|
|90|"nombre": "Tasa de errores de facturacion",|
|91|"caracteristica": "Libertad de Riesgo",|
|92|"valor": valor,|
|93|"unidad": "proporcion",|
|94|"umbral": UMBRAL_TASA_ERROR_FACT,|
|95|"cumple": valor <= UMBRAL_TASA_ERROR_FACT,|
|96|}|
|97||
|98||
|99<br>**d**|**ef** generar_reporte():|
|100|"""Orquesta el calculo de todas las metricas y consolida el resultado."""|
|101|logs, encuesta, incidentes = cargar_datos()|
|102||
|103|reporte = {|
|104|"efectividad": metrica_efectividad(logs),|
|105|"eficiencia": metrica_eficiencia(logs),|
|106|"satisfaccion": metrica_satisfaccion(encuesta),|
|107|_# Se asume un total simulado de 8500 transacciones de facturacion_|
|108|_# en el periodo de medicion (dato provisto por el area financiera)._|
|109|"libertad_riesgo": metrica_libertad_riesgo(incidentes, total_transacciones=8500),|
|110|}|
|111||
|112|eficiencia_sede = metrica_eficiencia_por_sede(logs)|
|113||
|114|**return** reporte, eficiencia_sede|
|115||
|116||
|117<br>**i**|**f** __name__ == "__main__":|
|118|reporte, eficiencia_sede = generar_reporte()|
|119||
|120|**print**("=== Reporte de Calidad en Uso - MediSalud HIS ===\n")|
|121|**for** clave, metrica **in** reporte.items():|
|122|estado = "CUMPLE" **if** metrica["cumple"] **else** "NO CUMPLE"|
|123|**print**(f"{metrica[’nombre’]}: {metrica[’valor’]} {metrica[’unidad’]} "|
|124|f"(umbral: {metrica[’umbral’]}) -> {estado}")|
|125||
|126|**print**("\n=== Eficiencia por sede (Cobertura de Contexto) ===")|
|127|**print**(eficiencia_sede.to_string(index=False))|



Listing 8.1: Módulo de cálculo automatizado de métricas ISO/IEC 25022 

### **Paso 2: Exportación de resultados a JSON** 

Añadir al final del script anterior (o en un módulo separado scripts/exportar_reporte.py): 

1 **<mark>import</mark>** <mark>json</mark> 2 **<mark>from</mark>** <mark>metricas_iso25022</mark> **<mark>import</mark>** <mark>generar_reporte</mark> 

3 4 <mark>reporte, eficiencia_sede = generar_reporte()</mark> 

CAPÍTULO 8. AUTOMATIZACIÓN DE LA MEDICIÓN 

43 

5 6 <mark>salida = {</mark> 7 <mark>"metricas": reporte,</mark> 8 <mark>"eficiencia_por_sede": eficiencia_sede.to_dict(orient="records"),</mark> 9 <mark>}</mark> 10 11 **<mark>with open</mark>** <mark>("dashboards/indicadores.json", "w", encoding="utf-8")</mark> **<mark>as</mark>** <mark>f:</mark> 12 <mark>json.dump(salida, f, indent=2, ensure_ascii=False)</mark> 13 14 **<mark>print</mark>** <mark>("Reporte exportado a dashboards/indicadores.json")</mark> 

Listing 8.2: Exportación de indicadores a JSON para consumo por dashboards 

**Paso 3: Automatización con GitHub Actions (integración continua de la medición)** 

Crear .github/workflows/medicion_calidad.yml: 

1 <mark>name: Medicion Calidad en Uso - MediSalud</mark> 2 3 <mark>on:</mark> 4 <mark>schedule:</mark> 5 <mark>- cron: "0 6 * * 1" # Cada lunes a las 06:00 UTC</mark> 6 <mark>workflow_dispatch: {}</mark> 7 8 <mark>jobs:</mark> 9 <mark>calcular-metricas:</mark> 10 <mark>runs-on: ubuntu-latest</mark> 11 <mark>steps:</mark> 12 <mark>- uses: actions/checkout@v4</mark> 13 <mark>- name: Configurar Python</mark> 14 <mark>uses: actions/setup-python@v5</mark> 15 <mark>with:</mark> 16 <mark>python-version: "3.11"</mark> 17 <mark>- name: Instalar dependencias</mark> 18 <mark>run: pip install pandas numpy</mark> 19 <mark>- name: Ejecutar calculo de metricas</mark> 20 <mark>run: python scripts/metricas_iso25022.py</mark> 21 <mark>- name: Exportar reporte JSON</mark> 22 <mark>run: python scripts/exportar_reporte.py</mark> 23 <mark>- name: Subir artefacto de indicadores</mark> 24 <mark>uses: actions/upload-artifact@v4</mark> 25 <mark>with:</mark> 26 <mark>name: indicadores-calidad-uso</mark> 27 <mark>path: dashboards/indicadores.json</mark> 

Listing 8.3: Workflow de GitHub Actions para ejecutar la medición automáticamente 

_Taller ISO/IEC 25022 — Calidad en Uso_ 

44 

Este flujo convierte el programa de medición de Calidad en Uso en un proceso **continuo y reproducible** , ejecutado automáticamente cada semana sin intervención manual, siguiendo el mismo principio que la integración continua aplica al código fuente. 

### **Resolución de Problemas** 

- **Error ModuleNotFoundError: No module named ’pandas’ en GitHub Actions:** verificar que el paso _Instalar dependencias_ se ejecuta antes del paso de cálculo, y que el nombre del paquete coincide exactamente (pandas, no Pandas). 

- **Error KeyError: ’modulo’ en metrica_libertad_riesgo:** indica que el CSV de incidentes no tiene la columna esperada; verificar el encabezado del archivo generado en el Escenario 2. 

- **El workflow de GitHub Actions no se ejecuta con cron:** GitHub puede retrasar unos minutos la ejecución programada bajo carga alta; para pruebas, usar el disparador manual workflow_dispatch. 

Es recomendable pedir a los estudiantes que además escriban una prueba unitaria simple con pytest para metrica_eficiencia, verificando que el promedio se calcula correctamente sobre un conjunto de datos controlado, reforzando así la relación entre pruebas de software y confiabilidad de las métricas. 

Al finalizar este escenario, el equipo dispone de un pipeline Python ejecutable localmente y en GitHub Actions, capaz de calcular las cuatro métricas principales y exportarlas en formato JSON, listo para alimentar los dashboards del Escenario 9. 

### **Preguntas de Discusión** 

1. ¿Qué ventajas ofrece programar la medición en GitHub Actions frente a ejecutarla manualmente cada trimestre? 

2. ¿Qué riesgo existe si el umbral (UMBRAL_TIEMPO_TAREA) queda «hardcodeado» en el script en lugar de estar en un archivo de configuración externo? 

### **Conclusiones Parciales** 

El estudiante ha automatizado por completo el cálculo de métricas de Calidad en Uso, transformando fórmulas normativas en código ejecutable, reproducible e integrable en un flujo de integración continua, una competencia directamente transferible a un entorno profesional de DevOps. 

