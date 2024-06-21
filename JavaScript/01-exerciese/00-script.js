/*Programa una función que te devuelva el texto recortado según el número de caracteres 
indicados, pe. miFuncion("Hola Mundo", 4) devolverá "Hola".*/

// funcion expresada
const recortarCadena = (cadena = "", longitud = undefined) => 
    (!cadena)
    ? console.warn("No ingresaste ninguna cadena")
    : console.info(cadena.slice(0,longitud));
    
    
recortarCadena("Hola mundo",4);