# Programa una función que cuente el número de caracteres de una cadena de texto,
# pe. miFuncion("Hola Mundo") devolverá 10.


def contarCaracteres(cadena = ""):
    if not cadena:
        raise ValueError("Debes ingresar una cadena")
    else:
        print(f"La cadena '{cadena}' tiene {len(cadena)} caracteres")

try:
    contarCaracteres()
except ValueError as e:
    print(f"error: {e}")
contarCaracteres("Hola mundo")
