# 📂 Proyecto de Automatizacion Urban Grocers

---

## 🌟 Descripcion del proyecto

Automatización de pruebas de caja negra a nivel de API para verificar los requisitos funcionales y de límites del campo name en el endpoint de creación de kits de productos (Main.Kits). El proyecto incluyó la gestión del ciclo de autenticación y la validación de respuestas JSON/códigos HTTP.

Este proyecto implementa pruebas automatizadas para la API de creación de kits (POST api/v1/kits). Dado que la creación de un kit requiere autenticación, el flujo de prueba comienza con la creación de un usuario (POST /api/v1/users) para obtener el AuthToken necesario, el cual se utiliza para autorizar la solicitud de creación del kit. 

La estructura del proyecto se basa en el framework requests de Python, separando la configuración (configuration.py), los datos de prueba (data.py), el envío de solicitudes (sender_stand_request.py) y la lógica de prueba y aserciones (create_kit_name_kit_test.py) para una mejor mantenibilidad y claridad. Las pruebas se centran en la validación funcional del campo name del kit

Se han creado varias listas de comprobación, haciendo varias pruebas en del campo name en la solicitud de creación de un kit de productos.
Las pruebas estan automatizadas y escritas basadas en la lista de comprobación proporcionada para el proyecto. Para consultar mas detalles adicionales o consultar la lista de comprobacion usada para el proyecto se puede consultar el archivo "Descripcion.pdf", incluido en la carpeta raiz del proyecto.
 

---
## 🛠 Estructura del proyecto

El proyecto esta compuesto de la siguiente estructura:
* `"configuration.py"`:  Almacena las variables de configuración clave del proyecto. Define la URL base del servicio (URL_SERVICE) y las rutas específicas para los endpoints de la API (CREATE_USER_PATH, CREATE_KITS_PATH).
* `"data.py"`: Contiene todos los datos de prueba (fixtures) y los encabezados (headers) necesarios para las solicitudes a la API. Incluye los cuerpos de solicitud para la creación de usuarios (user_body) y los nueve cuerpos de prueba para validar el campo name del kit (kit_body_test1 a kit_body_test9).
* `"sender_stand_request.py"`: Actúa como el módulo de envío de solicitudes (API client). Contiene funciones que realizan las peticiones HTTP (POST) a los endpoints, específicamente para crear un usuario (post_new_user) y crear un kit (post_new_client_kit).
* `"create_kit_name_kit_test.py"`: Es el archivo principal de las pruebas. Contiene la lógica para la autenticación (crear usuario y obtener authToken) y las funciones de aserción (positive_assert, negative_assert). Incluye la lista de 9 funciones de prueba que validan el campo name del kit.
* `"README.md"`: Este archivo.

---

## 🛠 Tecnologías y técnicas utilizadas.

Para la elaboracion de las pruebas Automatizadas se utilizó el lenguaje de programación Python. El framework de pruebas pytest. Y 
la librearia response para manejar las solicitudes que interactuan con las APIs. 

Se utilizo el sistema de control de versiones Git y se utilizo la plataforma web GitHub para alojar el proyecto.