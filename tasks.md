# Tasks

## 1. Base de Datos (PostgreSQL / Supabase)

### 1.1. Análisis y Diseño [[WIA-10](https://linear.app/remoto-now/issue/WIA-10/11-analisis-y-diseno-de-base-de-datos)]
- [x] Analizar el dataset de Kaggle y extraer los campos relevantes. _(Completado: Se documentaron los campos y su significado en README de database)_
- [x] Definir el modelo de datos normalizado (tablas, relaciones, claves primarias y foráneas). _(Completado: Modelo documentado y diagrama ER generado en README de database)_
- [x] Crear un diagrama entidad-relación (ER) para la base de datos. _(Completado: Ver src/database/README.md)_
- [x] Documentar el modelo de datos propuesto. _(Completado: Ver src/database/README.md)_

### 1.2. Implementación [[WIA-11](https://linear.app/remoto-now/issue/WIA-11/12-implementacion-de-base-de-datos)]
- [x] Crear el proyecto en Supabase. _(Completado: Proyecto 'saas-analytics' creado en la organización 'Workshop IA')_
- [x] Configurar la base de datos inicial en Supabase. _(Completado: Tablas y esquema creados según el modelo)_
- [x] Crear las tablas en Supabase/PostgreSQL según el modelo normalizado. _(Completado)_
- [x] Definir índices y restricciones necesarias para integridad y rendimiento. _(Completado)_
- [ ] Probar la inserción de datos de ejemplo para validar el modelo.

### 1.3. Carga de Datos [[WIA-12](https://linear.app/remoto-now/issue/WIA-12/13-carga-de-datos-en-base-de-datos)]
- [ ] Validar la integridad de los datos importados a través del endpoint.
- [ ] Documentar el proceso de carga manual mediante el endpoint.

---

## 2. Backend (FastAPI)

### 2.1. Configuración Inicial [[WIA-13](https://linear.app/remoto-now/issue/WIA-13/21-configuracion-inicial-del-backend)]
- [x] Inicializar proyecto base de FastAPI (entorno virtual, main.py, requirements.txt).
- [x] Definir estructura de carpetas siguiendo arquitectura de tres capas:
      - api/ (routers/endpoints)
      - services/ (lógica de negocio)
      - persistence/ (acceso a datos, conexión Supabase/PostgreSQL, modelos y repositorios)
      - core/ (configuración, utilidades, middlewares)
- [x] Configurar gestión de dependencias (FastAPI, Uvicorn, requests/httpx para Supabase, etc).
- [x] Configurar archivo de settings y variables de entorno (.env, config.py).
- [x] Implementar módulo de conexión a Supabase vía HTTP (requests/httpx).
- [x] Configurar CORS y middlewares básicos (logging, manejo de errores).
- [x] Crear endpoint de salud (healthcheck) y esqueleto de routers para endpoints futuros.
- [x] Verificar y personalizar la documentación automática (OpenAPI/Swagger).
- [x] Añadir instrucciones básicas en README para levantar el backend y probar el endpoint de salud.

### 2.2. Endpoints de API [[WIA-14](https://linear.app/remoto-now/issue/WIA-14/22-endpoints-de-api-backend)]
- [x] Implementar endpoint protegido para cargar manualmente el dataset (subida de archivo y procesamiento).
- [x] Implementar endpoint para obtener métricas generales del dashboard.
- [x] Implementar endpoint para obtener detalles de una empresa específica.
- [x] Validar y documentar los endpoints con OpenAPI/Swagger.

### 2.3. Lógica de Negocio [[WIA-15](https://linear.app/remoto-now/issue/WIA-15/23-logica-de-negocio-backend)]
- [x] Implementar lógica para procesar y transformar los datos del dataset según las necesidades del dashboard.
- [x] Gestionar errores y validaciones en los endpoints.

### 2.4. Pruebas [[WIA-16](https://linear.app/remoto-now/issue/WIA-16/24-pruebas-backend)]
- [x] Escribir pruebas unitarias para los endpoints y lógica de negocio. _(Incluye mocks y uso de dependency_overrides)_
- [x] Probar la integración con la base de datos. _(Mockeado para evitar dependencias externas)_
- [x] Documentar en README cómo ejecutar las pruebas automatizadas.

---

## 3. Frontend (Next.js)

### 3.1. Configuración Inicial [[WIA-17](https://linear.app/remoto-now/issue/WIA-17/31-configuracion-inicial-del-frontend)]
- [ ] Crear el proyecto base de Next.js.
- [ ] Definir la organización del frontend (estructura de carpetas, componentes, vistas, estilos, etc.).

### 3.2. Dashboard [[WIA-18](https://linear.app/remoto-now/issue/WIA-18/32-dashboard-frontend)]
- [ ] Implementar la página principal del dashboard.
- [ ] Consumir el endpoint de métricas generales y mostrar los datos.
- [ ] Implementar visualizaciones (gráficas, tablas, etc.) para las métricas clave.

### 3.3. Detalle de Empresa [[WIA-19](https://linear.app/remoto-now/issue/WIA-19/33-detalle-de-empresa-frontend)]
- [ ] Implementar la vista de detalle para una empresa específica.
- [ ] Consumir el endpoint de detalles de empresa.

### 3.4. UI/UX [[WIA-20](https://linear.app/remoto-now/issue/WIA-20/34-uiux-frontend)]
- [ ] Diseñar una interfaz clara y fácil de usar.
- [ ] Asegurar la responsividad y accesibilidad del dashboard.

---

## 4. Infraestructura y Despliegue [[WIA-21](https://linear.app/remoto-now/issue/WIA-21/4-infraestructura-y-despliegue)]

- [ ] Configurar Supabase para la base de datos.
- [ ] Configurar despliegue del backend (FastAPI) en un servicio gestionado.
- [ ] Configurar despliegue del frontend (Next.js) en Vercel u otro servicio gestionado.
- [ ] Documentar el proceso de despliegue.

---

## 5. Documentación [[WIA-22](https://linear.app/remoto-now/issue/WIA-22/5-documentacion)]

- [ ] Documentar la arquitectura general del sistema.
- [ ] Documentar el uso de la API y ejemplos de consumo.
- [ ] Documentar el proceso de carga de datos y administración.

---

## Discovered During Work
- [2025-07-10] Migración de Pydantic: Se reemplazó la clase interna Config por model_config = ConfigDict(...) en Settings para evitar warnings y cumplir con Pydantic v2+.
- [x] Optimización de bulk_insert en todos los repositorios (2024-06-18)
- [x] Agregar tests unitarios para bulk_insert en investor, industry, location y company_investor (2024-06-18) 