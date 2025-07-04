# Primer prompt

Eres un arquitecto de software senior especializado en escribir architecture decision records (ADR).

Analiza el archivo @planning.md y @tasks.md, e identifica las decisiones de diseño que más van a influir en el desarrollo del proyecto.

Las eleccciones tecnológicas más importantes deben ir en decisiones independientes. Por ejemplo, usar Next.js para el frontend.

Mejoras futuras al proyecto no deben ser consideradas como decisiones de diseño, ya que pueden cambiar a futuro.

Solo identifica y lista las decisiones. No escribas nada.

# Segundo prompt

Toma las decisiones de diseño que definiste y escribe un ADR para cada una de ellas, en el directorio `docs/adrs`.

El formato del nombre del archivo debe ser `01_nombre_decision.md`, `02_nombre_decision.md`, etc.

Hoy es 3 de julio de 2025.

Aquí tienes dos ejemplos de ADR:

```markdown
# 1. Interoperabilidad como atributo de calidad

Fecha: Julio 18 de 2024

## Status

Aceptada.

## Contexto

Un aspecto importante del nuevo sistema de reservas está relacionado con la administración de la limpieza.

Se usarán diversos dispositivos en los carros de limpiezas, con los cuales deberá interactuar el sistema.

## Decisión

Consideramos interoperabilidad como un atributo de calidad principal.

Entiéndase interoperabilidad como la capacidad sintáctica y semántica que tendrá nuestro sistema para intercambiar datos con todos los dispositivos a soportar.

## Consecuencias

Consideramos patrones de diseño que permitan soportar distintos dispositivos.

```markdown
# 2. Disponibilidad como atributo de calidad

Fecha: Julio 18 de 2024

## Status

Aceptada.

## Contexto

Dada la cercanía de la temporada alta, es fundamental garantizar que tanto el nuevo sistema como el existente estén disponibles para efectuar las reservas.

## Decisión

Consideramos disponibilidad como un atributo de calidad principal.

Entiéndase disponibilidad como un aspecto operativo y de infraestructura.

## Consecuencias

Se estudiará la infraestructura existente para definir tácticas que ayuden a mejorar la disponibilidad.

```