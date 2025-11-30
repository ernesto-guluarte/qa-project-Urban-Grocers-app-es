#===================DATOS PARA SOLICITUD DE USER===================#
user_headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

#===================DATOS PARA SOLICITUD DE KIT===================#
kit_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}

#===================CUERPOS PARA LAS PRUEBAS===================#

# Prueba 1. El número permitido de caracteres (1):
kit_body_test1 = {"name": "a"}
# Prueba 2. El número permitido de caracteres (511):
kit_body_test2 = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
# Prueba 3. El número de caracteres es menor que la cantidad permitida (0):
kit_body_test3 = {"name": ""}
# Prueba 4. El número permitido de caracteres (512):
kit_body_test4 = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
# Prueba 5. Se permiten caracteres especiales:
kit_body_test5 = {"name": "\"№%@\","}
# Prueba 6. Se permiten espacios:
kit_body_test6 = {"name": "A Aaa"}
# Prueba 7. Se permiten números
kit_body_test7 = {"name": "123"}
# # Prueba 8. El parámetro no se pasa en la solicitud:
kit_body_test8 = {}
# Prueba 9. Se ha pasado un tipo de parámetro diferente (número):
kit_body_test9 = {"name": 123}