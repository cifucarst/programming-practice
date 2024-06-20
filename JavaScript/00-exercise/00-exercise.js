/*
Programa una función que cuente el número de caracteres de una cadena de texto,
pe. miFuncion("Hola Mundo") devolverá 10. */

function contarCaracteres(cadena=""){
    if (!cadena){
        console.warn("No ingresaste ninguna cadena")
    }else{
        console.info(`La cadena "${cadena}" tiene ${cadena.length} caracteres`)
    }
};

contarCaracteres();
contarCaracteres("Hola mundo");


// funcion expresada
const contarCaracteres2 = (cadena = "") => 
(!cadena)
? console.warn("No ingresaste ninguna cadena")
: console.info(`La cadena "${cadena}" tiene ${cadena.length} caracteres`) 

contarCaracteres2();
contarCaracteres2("Hola mundo");