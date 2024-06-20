#!/bin/bash

# Función para contar el número de caracteres de una cadena de texto
contar_caracteres() {
    local cadena="$1"

    # Verificar si la entrada es no vacía
    if [ -z "$cadena" ]; then
        echo "Error: No se ha proporcionado una cadena de texto válida."
        return 1
    fi

    # Contar el número de caracteres
    local numero_de_caracteres=${#cadena}
    echo "$numero_de_caracteres"
}

# Ejemplo de uso
cadena="Hola Mundo"
resultado=$(contar_caracteres "$cadena")

# Verificar si la función tuvo éxito
if [ $? -eq 0 ]; then
    echo "El número de caracteres es: $resultado"  # Devolverá 10
else
    echo "Se produjo un error al contar los caracteres."
fi
