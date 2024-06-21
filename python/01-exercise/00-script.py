#!/usr/bin/env python3


# Programa una función que te devuelva el texto recortado según el número de caracteres 
# indicados, pe. miFuncion("Hola Mundo", 4) devolverá "Hola".


def cortar_cadena(cadena,longitud):
    """
    Recorta una cadena por el numero de longitud.

    Args:
        cadena (str): La cadena de texto la cual se recortara.
        longitud (int): El numero de caracteres por los que se recortara la cadena

    Returns:
        str: La cadena recortada.

    Raises:
        TypeError: Si el argumento proporcionado no es una cadena de texto o si
        la longitud no es un entero.
    """
    if not isinstance(cadena, str) or not cadena:
        raise TypeError("El argumento debe ser una cadena de texto.")
    
    if not isinstance(longitud, int) or not longitud:
        raise TypeError("El argumento debe ser un entero.")
    
    try:
        # Utilizamos rabanadas para recortar la cadena
        cadena_recortada = cadena[0:longitud]
        return cadena_recortada
    except Exception as e:
        # Capturamos cualquier excepción inesperada
        print(f"Ocurrió un error: {e}")
        raise

# Ejemplo de uso
try:
    resultado = cortar_cadena("Hola Mundo",4)
    print(f"El número de caracteres es: {resultado}")
except TypeError as e:
    print(e)
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")


# segundo ejemplo de uso
try:
    resultado = cortar_cadena("Hola mundo")
    print(f"El número de caracteres es: {resultado}")
except TypeError as e:
    print(e)
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")