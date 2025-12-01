# 🛒 Automatización de Pruebas de API para Urban Grocers

---

## 📝 Descripción del Proyecto

Este proyecto contiene un conjunto de **pruebas automatizadas de caja negra** desarrolladas en Python para validar el *backend* de la aplicación **Urban Grocers**.

El objetivo principal es verificar los requisitos funcionales y los límites (pruebas de límite y frontera) del campo `name` en el *endpoint* de creación de kits de productos (`POST /api/v1/kits`).

### Flujo de Pruebas

Dado que la creación de un kit requiere autenticación, el flujo de prueba automatizado se ejecuta en dos pasos clave:

1.  **Autenticación**: Se realiza la creación de un nuevo usuario (`POST /api/v1/users`) para obtener el **AuthToken** necesario.
2.  **Creación de Kits**: Se utiliza el **AuthToken** para autorizar y ejecutar las 9 pruebas de validación sobre el campo `name` al intentar crear un kit.

---

## 🛠️ Tecnologías y Técnicas

| Categoría | Tecnología/Técnica | Descripción                                                                                                                        |
| :--- | :--- |:-----------------------------------------------------------------------------------------------------------------------------------|
| **Lenguaje de Programación** | **Python** | Lenguaje principal utilizado para el desarrollo de las pruebas.                                                                    |
| **Framework de Pruebas** | **Pytest** | Utilizado para la estructura, detección y ejecución de los casos de prueba.                                                        |
| **Librería HTTP** | **Requests** | Implementa todas las solicitudes HTTP (`POST`) que interactúan con la API del servicio.                                            |
| **Patrón de Diseño** | **Separación de Capas** | El código está dividido en módulos para mejorar la legibilidad y la mantenibilidad (datos, configuración, cliente API, y pruebas). |

---

## 🏗️ Estructura y Función de los Archivos

El proyecto sigue una estructura modular para mantener la configuración, los datos y la lógica de las solicitudes separados de los casos de prueba, lo que facilita su mantenimiento.

| Archivo | Función Principal | Contenido Clave                                                                                                                                                                                                                     |
| :--- | :--- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `configuration.py` | **Configuración del Entorno** | Almacena la URL base del servicio (`URL_SERVICE`) y las rutas específicas de los *endpoints* (`CREATE_USER_PATH`, `CREATE_KITS_PATH`).                                                                                              |
| `data.py` | **Datos de Prueba** | Contiene todos los datos fijos, encabezados (`headers`) y, más importante, los **9 cuerpos de solicitud** (`kit_body_test1` a `kit_body_test9`) utilizados para validar el campo `name`.                                            |
| `sender_stand_request.py` | **Cliente API** | Funciona como la capa de abstracción para el envío de solicitudes. [cite_start]Contiene las funciones `post_new_user` y `post_new_client_kit` que construyen y envían las peticiones HTTP `POST`.                                   |
| `create_kit_name_kit_test.py` | **Lógica de Pruebas** | Contiene la lógica de autenticación (creación de usuario y obtención de *AuthToken*), las funciones de aserción (`positive_assert`, `negative_assert`) y las **9 funciones de prueba** que validan los requisitos del campo `name`. |

---

## 📝 Lista de Comprobación de Pruebas (Campo "name")

Las pruebas automatizadas se basan en la siguiente lista de comprobación proporcionada, cubriendo casos límite y casos de prueba funcionales (pruebas positivas y negativas).

| No. | Descripción de la Prueba | Código HTTP Esperado |
| :-- | :--- | :--- |
| 1 | Número permitido de caracteres (1) | 201 |
| 2 | Número permitido de caracteres (511) | 201 |
| 3 | Menos caracteres que el mínimo permitido (0) | 400 |
| 4 | Más caracteres que el máximo permitido (512) | 400 |
| 5 | Se permiten caracteres especiales (Ej: `№%@`) | 201 |
| 6 | Se permiten espacios | 201 |
| 7 | Se permiten números | 201 |
| 8 | El parámetro `name` no se pasa en la solicitud | 400 |
| 9 | Tipo de parámetro diferente (Ej: número en lugar de string) | 400 |

---

## 🚀 Ejecución de las Pruebas

Sigue estos pasos para configurar y ejecutar las pruebas en tu entorno local:

### 1. Requisitos Previos

Asegúrate de tener instalado **Python** en tu sistema.

### 2. Instalación de Dependencias

Necesitarás instalar las librerías `requests` y `pytest`. Abre tu terminal o símbolo del sistema y ejecuta:

```bash
pip install requests pytest
```

### 3. Ejecutar las Pruebas

Para ejecutar el conjunto completo de pruebas, navega hasta el directorio que contiene los archivos en tu terminal y utiliza el comando `pytest`:

```bash
pytest