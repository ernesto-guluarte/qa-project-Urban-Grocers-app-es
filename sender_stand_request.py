import configuration
import requests
import data

#===================SOLICITUDES PARA USUARIO===================#
#crear usuario
def post_new_user(user_body):
    # Realiza una solicitud POST
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # Concatenación de URL base y ruta.
                         json=user_body, # Datos a enviar en la solicitud.
                         headers=data.user_headers) # Encabezados de solicitud.

#===================SOLICITUDES PARA KITS===================#
#crear kit
def post_new_client_kit(kit_headers, kit_body):
    # Realiza una solicitud POST
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH, # Concatenación de URL base y ruta.
                         json=kit_body,  # Datos a enviar en la solicitud.
                         headers=kit_headers) # Encabezados de solicitud.
