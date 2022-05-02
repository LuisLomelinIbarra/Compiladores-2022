# Avance 3

Se resolvieron algunos errores con la semantica para encontrar el tipo de un arreglo textual. También se cambio a que todos los elementos que se declaren en la función principal, se declaren como su propia entrada en la tabla en vez de que sea una addición a la tabla global. También se arreglo el error a la hora de declarar precedencia entre los operadores.

El avance de ahora debe de:
- Generar código intermedio en un archivo de cuadruplos

COSAS QUE INVESTIGAR:
- Hay que manejar bien la asignación de espacios en memoria de los cuadruplos para la generación de código intermedio. Por el momento solo va agregando de manera ascendente a un registro teoreticamente infinito
