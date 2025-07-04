# 1. Arquitectura de tres capas

Fecha: Julio 3 de 2025

## Status

Aceptada.

## Contexto

El sistema requiere una separación clara de responsabilidades para facilitar el desarrollo, mantenimiento y escalabilidad. Se busca desacoplar la presentación, la lógica de negocio y el almacenamiento de datos.

## Decisión

Se adopta una arquitectura de tres capas compuesta por:
- Frontend desarrollado en Next.js
- Backend desarrollado en FastAPI
- Base de datos PostgreSQL gestionada en Supabase

## Consecuencias

Permite escalar y mantener cada componente de forma independiente. Facilita la integración de nuevas tecnologías en cada capa y mejora la seguridad y la organización del código. 