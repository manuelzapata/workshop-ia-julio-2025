# Tasks

## 1. Base de Datos (PostgreSQL / Supabase)

### 1.1. Análisis y Diseño
- [ ] Analizar el dataset de Kaggle y extraer los campos relevantes.
- [ ] Definir el modelo de datos normalizado (tablas, relaciones, claves primarias y foráneas).
- [ ] Crear un diagrama entidad-relación (ER) para la base de datos.
- [ ] Documentar el modelo de datos propuesto.

### 1.2. Implementación
- [ ] Crear las tablas en Supabase/PostgreSQL según el modelo normalizado.
- [ ] Definir índices y restricciones necesarias para integridad y rendimiento.
- [ ] Probar la inserción de datos de ejemplo para validar el modelo.

### 1.3. Carga de Datos
- [ ] Validar la integridad de los datos importados a través del endpoint.
- [ ] Documentar el proceso de carga manual mediante el endpoint.

---

## 2. Backend (FastAPI)

### 2.1. Configuración Inicial
- [ ] Crear el proyecto base de FastAPI.
- [ ] Configurar la conexión a la base de datos (Supabase/PostgreSQL).
- [ ] Definir la estructura de carpetas del backend.

### 2.2. Endpoints de API
- [ ] Implementar endpoint protegido para cargar manualmente el dataset (subida de archivo y procesamiento).
- [ ] Implementar endpoint para obtener métricas generales del dashboard.
- [ ] Implementar endpoint para obtener detalles de una empresa específica.
- [ ] Validar y documentar los endpoints con OpenAPI/Swagger.

### 2.3. Lógica de Negocio
- [ ] Implementar lógica para procesar y transformar los datos del dataset según las necesidades del dashboard.
- [ ] Gestionar errores y validaciones en los endpoints.

### 2.4. Pruebas
- [ ] Escribir pruebas unitarias para los endpoints y lógica de negocio.
- [ ] Probar la integración con la base de datos.

---

## 3. Frontend (Next.js)

### 3.1. Configuración Inicial
- [ ] Crear el proyecto base de Next.js.
- [ ] Definir la organización del frontend (estructura de carpetas, componentes, vistas, estilos, etc.).

### 3.2. Dashboard
- [ ] Implementar la página principal del dashboard.
- [ ] Consumir el endpoint de métricas generales y mostrar los datos.
- [ ] Implementar visualizaciones (gráficas, tablas, etc.) para las métricas clave.

### 3.3. Detalle de Empresa
- [ ] Implementar la vista de detalle para una empresa específica.
- [ ] Consumir el endpoint de detalles de empresa.

### 3.4. UI/UX
- [ ] Diseñar una interfaz clara y fácil de usar.
- [ ] Asegurar la responsividad y accesibilidad del dashboard.

---

## 4. Infraestructura y Despliegue

- [ ] Configurar Supabase para la base de datos.
- [ ] Configurar despliegue del backend (FastAPI) en un servicio gestionado.
- [ ] Configurar despliegue del frontend (Next.js) en Vercel u otro servicio gestionado.
- [ ] Documentar el proceso de despliegue.

---

## 5. Documentación

- [ ] Documentar la arquitectura general del sistema.
- [ ] Documentar el uso de la API y ejemplos de consumo.
- [ ] Documentar el proceso de carga de datos y administración. 