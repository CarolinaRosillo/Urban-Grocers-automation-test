import sender_stand_request
import data


# Función para generar el cuerpo de la solicitud para crear un kit de producto con el nombre especificado.
def get_kit_body(name):
    current_body = data.kit_body.copy()  # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body["name"] = name  # Se cambia el valor del parámetro name
    return current_body  # Se devuelve un nuevo diccionario con el valor name requerido


# Función para realizar una prueba positiva
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Imprimir el cuerpo de la respuesta
    print("Response body:", kit_response.json())

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


# Función para realizar pruebas negativa (código de respuesta 400)
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)

    print("Response body:", response.json())

    # Comprueba si el código de estado es 400
    assert response.status_code == 400


# Prueba 1: Número mínimo permitido de caracteres (1)
# Se espera que la solicitud se realice con éxito y devuelva un código de respuesta 201.
def test_1_character_in_kit_name_get_success_response():
    positive_assert("a")


# Prueba 2: Número máximo permitido de caracteres (511)
# Se espera que la solicitud se realice con éxito y devuelva un código de respuesta 201.
def test_511_characters_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
# Se espera que la solicitud falle y devuelva un código de respuesta 400.
def test_0_characters_in_kit_name_get_error_response():
    negative_assert_code_400("")


# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
# Se espera que la solicitud falle y devuelva un código de respuesta 400.
def test_512_characters_in_kit_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Prueba 5: Se permiten caracteres especiales
# Se espera que la solicitud se realice con éxito y devuelva un código de respuesta 201.
def test_special_characters_in_kit_name_get_success_response():
    positive_assert("№%&@")


# Prueba 6: Se permiten espacios
# Se espera que la solicitud se realice con éxito y devuelva un código de respuesta 201.
def test_spaces_in_kit_name_get_success_response():
    positive_assert(" A Aaa ")


# Prueba 7: Se permiten números
# Se espera que la solicitud se realice con éxito y devuelva un código de respuesta 201.
def test_numbers_in_kit_name_get_success_response():
    positive_assert("123")


# Prueba 8: El parámetro no se pasa en la solicitud
# Se espera que la solicitud falle y devuelva un código de respuesta 400.
def test_omitted_parameter_in_kit_body_get_error_response():
    negative_assert_code_400({})


# Prueba 9: Se ha pasado un tipo de parámetro diferente (número)
# Se espera que la solicitud falle y devuelva un código de respuesta 400.
def test_different_parameter_in_kit_name_get_error_response():
    negative_assert_code_400(123)







