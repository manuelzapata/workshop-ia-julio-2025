# Tasks

## 1. Base de Datos (PostgreSQL / Supabase)

### 1.1. Análisis y Diseño [[WIA-10](https://linear.app/remoto-now/issue/WIA-10/11-analisis-y-diseno-de-base-de-datos)]
- [ ] Analizar el dataset de Kaggle y extraer los campos relevantes.
- [ ] Definir el modelo de datos normalizado (tablas, relaciones, claves primarias y foráneas).
- [ ] Crear un diagrama entidad-relación (ER) para la base de datos.
- [ ] Documentar el modelo de datos propuesto.

### 1.2. Implementación [[WIA-11](https://linear.app/remoto-now/issue/WIA-11/12-implementacion-de-base-de-datos)]
- [ ] Crear el proyecto en Supabase.
- [ ] Configurar la base de datos inicial en Supabase.
- [ ] Crear las tablas en Supabase/PostgreSQL según el modelo normalizado.
- [ ] Definir índices y restricciones necesarias para integridad y rendimiento.
- [ ] Probar la inserción de datos de ejemplo para validar el modelo.

### 1.3. Carga de Datos [[WIA-12](https://linear.app/remoto-now/issue/WIA-12/13-carga-de-datos-en-base-de-datos)]
- [ ] Validar la integridad de los datos importados a través del endpoint.
- [ ] Documentar el proceso de carga manual mediante el endpoint.

---

## 2. Backend (FastAPI)

### 2.1. Configuración Inicial [[WIA-13](https://linear.app/remoto-now/issue/WIA-13/21-configuracion-inicial-del-backend)]
- [ ] Crear el proyecto base de FastAPI.
- [ ] Configurar la conexión a la base de datos (Supabase/PostgreSQL).
- [ ] Definir la estructura de carpetas del backend.

### 2.2. Endpoints de API [[WIA-14](https://linear.app/remoto-now/issue/WIA-14/22-endpoints-de-api-backend)]
- [ ] Implementar endpoint protegido para cargar manualmente el dataset (subida de archivo y procesamiento).
- [ ] Implementar endpoint para obtener métricas generales del dashboard.
- [ ] Implementar endpoint para obtener detalles de una empresa específica.
- [ ] Validar y documentar los endpoints con OpenAPI/Swagger.

### 2.3. Lógica de Negocio [[WIA-15](https://linear.app/remoto-now/issue/WIA-15/23-logica-de-negocio-backend)]
- [ ] Implementar lógica para procesar y transformar los datos del dataset según las necesidades del dashboard.
- [ ] Gestionar errores y validaciones en los endpoints.

### 2.4. Pruebas [[WIA-16](https://linear.app/remoto-now/issue/WIA-16/24-pruebas-backend)]
- [ ] Escribir pruebas unitarias para los endpoints y lógica de negocio.
- [ ] Probar la integración con la base de datos.

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