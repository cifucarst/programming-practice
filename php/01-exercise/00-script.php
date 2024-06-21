<?php
/**
 * Función para recortar una cadena según el número de caracteres indicados.
 *
 * @param string $cadena La cadena de texto a recortar.
 * @param int $longitud La longitud a la cual recortar la cadena.
 * @return string La cadena recortada.
 */
function cortarCadena($cadena, $longitud) {
    // Verificar que la longitud es un entero positivo
    if (!is_int($longitud) || $longitud < 0) {
        return "Error: La longitud debe ser un entero positivo.";
    }

    // Verificar que la cadena no esté vacía
    if (empty($cadena)) {
        return "Error: La cadena de texto no puede estar vacía.";
    }

    // Recortar la cadena y devolver el resultado
    return substr($cadena, 0, $longitud);
}

// Ejemplo de uso
$cadena = "Hola Mundo";
$longitud = 4;
$resultado = cortarCadena($cadena, $longitud);
echo $resultado; // Salida: Hola
?>