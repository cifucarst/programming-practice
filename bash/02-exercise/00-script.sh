#!/bin/bash

# Programa una funcion que dada una string te devuelva un array de textos separados
# por cierto caracter. miFuncion("Hola que tal", "") devolvera. ["Hola", "que", "tal"]

#!/bin/bash

function separar_texto_por_caracter() {
  # Validar tipo de dato de `texto`
  if [[ ! $1 =~ ^[[:alpha:]\ ]+$ ]]; then
    echo "Error: El primer argumento debe ser una cadena de texto."
    return 1
  fi

  # Validar longitud del `caracter_separador`
  if [[ ${#2} -ne 1 ]]; then
    echo "Error: El segundo argumento debe ser un único caracter."
    return 1
  fi

  # Separar la cadena de texto usando el separador
  array_subcadenas=(${1//"$2"/ })

  # Imprimir el array de subcadenas
  echo "${array_subcadenas[@]}"
}


# Ejemplo 1: Separar "Hola que tal" por " "
resultado=$(separar_texto_por_caracter "Hola que tal" " ")
echo "Resultado: $resultado"

# Ejemplo 2: Separar "Hola,Mundo" por ","
resultado=$(separar_texto_por_caracter "Hola,Mundo" ",")
echo "Resultado: $resultado"