# Proyecto Evaluación Sumativa 2 - Django Backend

## 📌 Descripción del Proyecto
**Objetivo:** Evolucionar el prototipo web modular de la Evaluación 1, migrando la gestión de información desde archivos JSON hacia una base de datos relacional nativa y administrable.
**Temática elegida:** Gestión deportiva de dos disciplinas independientes (Roster oficial de la UFC y grilla de pilotos de MotoGP).
**Funcionalidades implementadas:** 
- Base de datos relacional estructurada con llaves foráneas (ForeignKey).
- Panel de administración nativo (Django Admin) para la gestión CRUD completa.
- Interfaz gráfica construida con Bootstrap 5, conectada mediante Django ORM para la visualización de datos.

## 🏗️ Arquitectura y Tecnologías
- **Framework:** Django (Python).
- **Base de Datos:** SQLite (Migración a base de datos relacional).
- **Control de Versiones:** Git y GitHub.
- **Despliegue (Producción):** Instancia Linux en Amazon Web Services (AWS EC2).

## 📂 Estructura de Aplicaciones
1. **ufcApp:** Módulo encargado de gestionar Categorías, Gimnasios y Peleadores de artes marciales mixtas.
2. **motogpApp:** Módulo encargado de gestionar Categorías, Escuderías y Pilotos de motociclismo.