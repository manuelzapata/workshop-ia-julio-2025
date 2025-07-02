# Descripción General  
Esta aplicación proporciona un dashboard web dirigido a inversionistas, mostrando métricas clave de las principales empresas SaaS a partir de un dataset de Kaggle. El objetivo es facilitar la toma de decisiones de inversión mediante la visualización y exploración de datos relevantes. El dashboard es público y no requiere autenticación.

# Funcionalidades Principales  
- **Dashboard con métricas**: Visualización de métricas como ingresos anuales, número de empleados, valoración de la empresa, rondas de inversión y localización geográfica.
  - *Importancia*: Permite a los inversionistas identificar oportunidades y analizar el panorama del sector SaaS.
  - *Funcionamiento*: El frontend consulta al backend, que a su vez obtiene los datos de una base de datos PostgreSQL alimentada por el dataset de Kaggle.
- **Endpoint para carga de dataset**: Permite cargar manualmente el dataset de empresas SaaS al backend.
  - *Importancia*: Facilita la actualización de la información mostrada en el dashboard.
  - *Funcionamiento*: Un endpoint protegido en el backend permite subir el archivo del dataset y actualizar la base de datos.
- **Deep research sobre empresas**: (A definir en el futuro) Permitirá a los usuarios explorar en profundidad la información de una empresa específica.

# Experiencia de Usuario  
- **Perfiles de usuario**: No existen perfiles; el dashboard es público.
- **Flujos clave de usuario**: 
  - Acceso al dashboard y visualización de métricas.
  - Selección de una empresa para ver detalles (deep research, próximamente).
- **Consideraciones de UI/UX**: Interfaz clara, visualizaciones intuitivas y navegación sencilla para facilitar la exploración de datos.

# Arquitectura  
- **Componentes del sistema**:
  - Frontend: Next.js
  - Backend: FastAPI (Python)
  - Base de datos: PostgreSQL (Supabase)
- **Modelo de datos**: Estructura normalizada basada en el dataset de Kaggle.
- **APIs e integraciones**: 
  - API REST para consulta de métricas y detalles de empresas.
  - Endpoint para carga manual del dataset.
- **Requisitos de infraestructura**: Despliegue en servicios gestionados (por ejemplo, Vercel para frontend, Supabase para base de datos).

# Hoja de Ruta de Desarrollo  
- **Fase 1: Versión inicial**
  - Implementar backend con FastAPI y endpoint para carga manual del dataset.
  - Crear modelo de datos en PostgreSQL (Supabase).
  - Desarrollar frontend en Next.js para mostrar el dashboard con métricas básicas.
- **Fase 2: Mejoras futuras**
  - Añadir funcionalidad de deep research sobre empresas.
  - Automatizar la actualización del dataset.
  - Incorporar autenticación y perfiles de usuario si se requiere acceso restringido.

# Riesgos y Mitigaciones  
- **Desafíos técnicos**: Integración entre FastAPI y Supabase, normalización del dataset.
  - *Mitigación*: Comenzar con un modelo de datos simple y evolucionarlo según necesidades.
- **Versión inicial**: Dashboard público con carga manual del dataset y visualización de métricas básicas.
- **Limitaciones de recursos**: El alcance inicial es reducido para asegurar factibilidad y mantenibilidad.

# Apéndice  
- **Hallazgos de investigación**: El dataset de Kaggle proporciona información relevante para inversionistas, aunque no incluye métricas de crecimiento porcentual.
- **Especificaciones técnicas**: Uso de Next.js, FastAPI y Supabase como stack principal. 