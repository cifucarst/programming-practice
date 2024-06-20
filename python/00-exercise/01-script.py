def miFuncion(cadena):
    """
    Cuenta el número de caracteres de una cadena de texto.

    Args:
        cadena (str): La cadena de texto de la cual se contarán los caracteres.

    Returns:
        int: El número de caracteres en la cadena.

    Raises:
        TypeError: Si el argumento proporcionado no es una cadena de texto.
    """
    if not isinstance(cadena, str):
        raise TypeError("El argumento debe ser una cadena de texto.")
    
    try:
        # Utilizamos la función len() para contar el número de caracteres en la cadena
        numero_de_caracteres = len(cadena)
        return numero_de_caracteres
    except Exception as e:
        # Capturamos cualquier excepción inesperada
        print(f"Ocurrió un error: {e}")
        raise

# Ejemplo de uso
try:
    resultado = miFuncion("Hola Mundo")
    print(f"El número de caracteres es: {resultado}")  # Devolverá 10
except TypeError as e:
    print(e)
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
