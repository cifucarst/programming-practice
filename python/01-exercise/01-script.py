#!/usr/bin/env python3


def cortar_cadena(cadena, longitud):
    """
    Recorta una cadena por el número de longitud indicado.

    Args:
        cadena (str): La cadena de texto la cual se recortara.
        longitud (int): El número de caracteres por los que se recortará la cadena.

    Returns:
        str: La cadena recortada.

    Raises:
        TypeError: Si el argumento `cadena` no es una cadena de texto o si
        el argumento `longitud` no es un entero positivo.
    """
    if not isinstance(cadena, str) or not cadena:
        raise TypeError(f"Se esperaba una cadena de texto, pero se recibió: {type(cadena)}".format(type(cadena)))

    if not isinstance(longitud, int) or longitud <= 0:
        raise ValueError("El argumento 'longitud' debe ser un entero positivo.")

    try:
        cadena_recortada = cadena[:longitud]
        return cadena_recortada
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        raise

# Ejemplo de uso
try:
    resultado = cortar_cadena(3, 4)
    print(f"El resultado es: {resultado}")
except TypeError as e:
    print(e)
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")

# Segundo ejemplo de uso
try:
    resultado = cortar_cadena("Hola mundo", 5)
    print(f"El resultado es: {resultado}")
except TypeError as e:
    print(e)
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")