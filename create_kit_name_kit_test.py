import sender_stand_request
import data

#===================CREAR NUEVO USUARIO===================#

def create_user():
    # El resultado de la solicitud para crear un nuevo usuario se guarda en la variable response
    user_response = sender_stand_request.post_new_user(data.user_body)
    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Retornar la respuesta de la solicitud
    return user_response

#===================OBTENER EL AUTHTOKEN DE USUARIO===================#

def get_new_user_token(user_response):
    # Guarda el authToken en una variable
    auth_token = user_response.json()["authToken"]
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert auth_token != ""
    # Retorna el valor de auth_token
    return auth_token

#===================HEADERS DE KIT===================#

def get_kit_headers(auth_token): # Función para cambiar el valor del parámetro Authorization en el cuerpo de la solicitud de kit
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_headers = data.kit_headers.copy()
    # Se cambia el valor del parámetro Authorization
    current_headers["Authorization"] = "Bearer " + auth_token
    # Se devuelve un nuevo diccionario con el valor Authorization requerido
    return current_headers

#===================BODY DE KIT===================#

def get_kit_body(name): # Función para cambiar el valor del parámetro name en el cuerpo de la solicitud de kit
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

#===================FUNCIONES PARA CREAR UN KIT===================#

def create_kit(kit_name):
    # Crear nuevo usuario
    user_response = create_user()
    # Obtener el auth_token del usuario
    auth_token = get_new_user_token(user_response)

    # Enviar el auth_token a los headers del kit
    kit_headers = get_kit_headers(auth_token)
    # Enviar el name en el body del kit
    kit_body = get_kit_body(kit_name)

    # Crear kit y guardar el resultado de la respuesta de kit
    kit_response = sender_stand_request.post_new_client_kit(kit_headers, kit_body)

    #retornar la respuesta de kit
    return kit_response


def create_kit_without_name():# Función para crear un kit sin el parámetro 'name' en el cuerpo
    user_response = create_user()
    auth_token = get_new_user_token(user_response)
    kit_headers = get_kit_headers(auth_token)
    kit_response = sender_stand_request.post_new_client_kit(kit_headers, {})
    return kit_response

#===================FUNCION DE PRUEBA POSITIVA===================#

def positive_assert(kit_name):
    #Crear kit y guardar el resultado de la respuesta de kit
    kit_response = create_kit(kit_name)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201

    """Comprueba que el campo "name" del cuerpo de la respuesta
    coincide con el campo "name" del cuerpo de la solicitud"""
    assert kit_response.json()["name"] == kit_name

#===================FUNCIONES DE PRUEBAS NEGATIVAS===================#

def negative_assert(kit_name):
    # Crear kit y guardar el resultado de la respuesta de kit
    kit_response = create_kit(kit_name)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

# Función de prueba negativa para la prueba 8
def negative_assert_no_name():
    kit_response = create_kit_without_name()
    assert kit_response.status_code == 400

#===================LISTA DE COMPROBACION DE PRUEBAS===================#

# Prueba 1. El número permitido de caracteres (1):
def test_create_kit_1_letters_in__name_get_success_response():
    positive_assert("a")

# Prueba 2. El número permitido de caracteres (511):
def test_create_kit_511_letters_in__name_get_success_response():
    string511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert(string511)

# Prueba 3. El número de caracteres es menor que la cantidad permitida (0):
def test_create_kit_0_letters_in__name_get_failed_response():
    negative_assert("")

# Prueba 4. El número permitido de caracteres (512):
def test_create_kit_512_letters_in__name_get_failed_response():
    string512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    negative_assert(string512)

# Prueba 5. Se permiten caracteres especiales:
def test_create_kit_special_letters_in__name_get_success_response():
    positive_assert("\"№%@\"," )

# Prueba 6. Se permiten espacios:
def test_create_kit_space_between_letters_in__name_get_success_response():
    positive_assert("A Aaa")

# Prueba 7. Se permiten números
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

# Prueba 8. El parámetro no se pasa en la solicitud:
def test_create_kit_whitout_name_get_failed_response():
    negative_assert_no_name()

# Prueba 9. Se ha pasado un tipo de parámetro diferente (número):
def test_create_kit_number_type_name_get_failed_response():
    negative_assert(123)