# API de Transferencias

## Información del proyecto

**Aprendiz:** Sebastián Orrego

**Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO)

**Proyecto:** API REST para gestión de transferencias

**Tecnología principal:** Python
## Objetivo

Desarrollar una API REST utilizando Python y FastAPI para gestionar información relacionada con transferencias, permitiendo realizar operaciones de consulta, creación, actualización e inhabilitación de registros.

## Tecnologías utilizadas

- **Python:** lenguaje utilizado para desarrollar la API.
- **FastAPI:** framework utilizado para construir la API REST.
- **Pydantic:** utilizado para definir y validar los datos de las transferencias.
- **Uvicorn:** servidor utilizado para ejecutar la aplicación.
- **SQLite:** base de datos utilizada para almacenar las transferencias.
- **Git:** sistema utilizado para controlar las versiones del proyecto.

## Instalación

1. Clonar o descargar el proyecto.
2. Crear un entorno virtual de Python.
3. Activar el entorno virtual.
4. Instalar las dependencias del proyecto con el siguiente comando:

```bash
pip install -r requirements.txt
## Ejecución

Para iniciar la API, ejecutar el siguiente comando en la terminal:

```bash
uvicorn main:app --reload

La API estará disponible en:

http://127.0.0.1:8000

La documentación interactiva de Swagger estará disponible en:

http://127.0.0.1:8000/docs


## Endpoints

 Método  URL  Descripción 
 GET  `/api/transferencias`  Consulta todas las transferencias 
 GET  `/api/transferencias/{id_pago}`  Consulta una transferencia por su identificador 
 POST  `/api/transferencias`  Crea una nueva transferencia 
 PUT  `/api/transferencias/{id_pago}`  Actualiza una transferencia existente 
 DELETE  `/api/transferencias/{id_pago}`  Inhabilita una transferencia cambiando su estado a Inactiva 

## Estructura de una transferencia

Una transferencia contiene los siguientes campos:

 Campo  Tipo  Descripción 

 `cliente`  String  Nombre del cliente que realiza la transferencia 
 `valor`  Float  Valor de la transferencia |
 `fecha`  String Fecha en la que se realizó la transferencia 
 `hora`  String  Hora en la que se realizó la transferencia 
 `banco`  String  Banco relacionado con la transferencia 
 `id_pago`  String  Identificador único de la transferencia 
 `estado` String  Estado actual de la transferencia 

## Ejemplo de transferencia

```json
{
  "cliente": "Maria Jose Melo",
  "valor": 100000,
  "fecha": "14/09/2026",
  "hora": "13:50",
  "banco": "Bancolombia",
  "id_pago": "78843754",
  "estado": "Inactiva"
}

## Estado del proyecto

La API REST cuenta con operaciones para crear, consultar, actualizar e inhabilitar transferencias mediante los métodos HTTP GET, POST, PUT y DELETE.

La documentación interactiva de la API puede consultarse mediante Swagger.