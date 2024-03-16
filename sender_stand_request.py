import configuration
import requests
import data


# Función para recibir el token de autenticación
def auth_token():
    user = post_new_user(data.user_body)  # Crea un nuevo usuario
    user_json = user.json()  # Obtiene el cuerpo de la respuesta en formato JSON
    return user_json['authToken']  # Extrae y devuelve el token de autenticación


# Función para crear un usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Función para crear un nuevo kit de producto
def post_new_client_kit(kit_body):
    token = auth_token()  # Obtiene el token de autenticación del usuario
    headers = data.headers.copy()  # Copia los encabezados definidos en el módulo 'data'
    headers['Authorization'] = f'Bearer {token}'  # Agrega el token de autenticación a los encabezados

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers)


response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())