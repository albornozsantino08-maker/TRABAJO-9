# Sistema de Gestión Deportiva

TP N° 9 – Base de Datos 1 2026 – IPET 247

Programa de consola en Python que permite gestionar los jugadores de un club:
ver la lista, agregar jugadores nuevos, modificar sus datos y eliminarlos.
Toda la información se guarda en una base de datos MySQL.

## Operaciones CRUD
| Operación | Opción del menú | Qué hace |
|-----------|-----------------|----------|
| Leer | 1 | Permite ver los datos de los jugadores cargados |
| Crear | 2 | Permite crear nuevos datos de nuevos jugadores |
| Actualizar | 3 | Permite modificar datos de jugadores ya creados |
| Eliminar | 4 | Permite eliminar datos de jugadores cargados |

## Tecnologías
- Python
- MySQL (XAMPP)
- Librerías: `mysql-connector-python`, `python-dotenv`

## Requisitos
- Python 3.8 o superior
- XAMPP con MySQL iniciado

## Instalación y uso
1. Descargar este repositorio.
2. Iniciar **MySQL** desde el panel de XAMPP.
3. Abrir phpMyAdmin e importar el archivo `base_datos.sql`. Esto crea la base `trabajo_7` con sus tablas.
4. Instalar las librerías:
   ```
   pip install -r requirements.txt
   ```
5. Copiar `.env.example` como `.env` y completar con los datos de conexión.
6. Ejecutar:
   ```
   python gestion_deportiva.py
   ```

## Seguridad
Las credenciales de conexión no están en el repositorio. Se leen desde un archivo
`.env` que está incluido en `.gitignore`. Los datos reales se entregan por separado en Classroom.

## Autor
[ALBORNOZ y 6TO E]
