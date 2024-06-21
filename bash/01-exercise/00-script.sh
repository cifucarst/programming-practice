#!/bin/bash

# Programa una función que te devuelva el texto recortado según el número de caracteres 
# indicados, pe. miFuncion("Hola Mundo", 4) devolverá "Hola".

# Funcion para recortar una cadena por el numero indicado.
function cortarCadena() {
    local cadena="$1"
    local longitud=$2

    # Verificar si la cadena de texto no está vacía
    if [[ -z "$cadena" ]]; then
        echo "Error: No se ha proporcionado una cadena de texto válida."
        return 1
    fi

    # Verificar si la longitud es un entero positivo
    if ! [[ "$longitud" =~ ^[0-9]+$ ]]; then
        echo "Error: No se ha proporcionado una longitud válida, debes ingresar un entero positivo."
        return 1
    fi

    # Cortar la cadena y devolver el resultado
    local recortada="${cadena:0:longitud}"
    echo "La cadena recortada es: $recortada"
}

# Llamar a la funcion con los argumentos proporcionados
cortarCadena "hola mundo" 4

# ejemplos
cortarCadena "hola mundo" 