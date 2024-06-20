<?php
function contarCaracteres($cadena) {
    // Verificar si el argumento proporcionado es una cadena de texto
    if (!is_string($cadena)) {
        throw new InvalidArgumentException("El argumento debe ser una cadena de texto.");
    }

    // Contar el número de caracteres
    $numero_de_caracteres = strlen($cadena);
    return $numero_de_caracteres;
}

try {
    // Ejemplo de uso
    $cadena = "Hola Mundo";
    $resultado = contarCaracteres($cadena);
    echo "El número de caracteres es: $resultado";  // Devolverá 10
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    echo "Se produjo un error inesperado: " . $e->getMessage();
}
?>