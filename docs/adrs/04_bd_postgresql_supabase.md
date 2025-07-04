# 4. Base de datos PostgreSQL con Supabase

Fecha: Julio 3 de 2025

## Status

Aceptada.

## Contexto

Se requiere una base de datos relacional robusta, escalable y gestionada en la nube, que permita integrarse fácilmente con el stack seleccionado y ofrezca herramientas de administración modernas.

Adicionalmente, todos los sistemas en la empresa utilizan PostgreSQL y Supabase, y por lineamientos de arquitectura no se permite el uso de otro motor de base de datos.

## Decisión

Se selecciona PostgreSQL gestionado por Supabase como base de datos principal del sistema.

## Consecuencias

Permite aprovechar la robustez de PostgreSQL y la facilidad de gestión y despliegue de Supabase. Facilita la integración con otros servicios y el acceso seguro a los datos. 