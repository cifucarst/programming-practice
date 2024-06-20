#!/bin/bash

# Programa una función que cuente el número de caracteres de una cadena de texto,
# pe. miFuncion("Hola Mundo") devolverá 10.

function contarCaracteres(){
    cadena="$1"
    if [ ! $cadena ];then
        echo "Debes ingresar una cadena de texto"
    else
        echo "La cadena '$cadena' tiene ${#cadena} caracteres"
    fi
}

contarCaracteres
contarCaracteres "Hola mundo"