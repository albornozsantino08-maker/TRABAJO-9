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

# Ficha de declaración de IA

## herramienta
CloudeIA

## proposito
°Guía paso a paso para instalar y configurar XAMPP y Python.
°Explicación de cómo conectar Python con MySQL.
°Ayuda para entender los mensajes de error.
°Estructura del README.

## prompt utilizado
acá están los archivos ejemplo y consigna de mi trabajo número 9, en base a mi trabajo número 8 y 7 puedes ayudarme a entender lo que debo realizar en el siguiente trabajo respetando las consignas? 

## edicion
Correcion de script SQL (los ;, Posicion, AUTO_INCREMENT).
Repacion de errores: nombres de columnas, de tabla, sangría y nombres de funciones.

## aprendizaje
aprendí a como conectar el xampp con el vs code y la gran cantidad de diferencias que tiene a la hora de hacer que una base de datos funcione como los códigos obligatorio como el DELETE FROM __ WHERE __. ya que sin el where el delete borraría todo el código. 
