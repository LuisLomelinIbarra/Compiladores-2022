# Avance 2

Se avanzo con la generacion del directorio de funciones y la tabla de variables. Ádemas se creo el cubo semántico para las operaciones del lenguaje. De igual manera se empezo a implementar el análisis semántico de las operaciones del lenguaje. Al realizar esto se tuvo que reestructurar algunas reglas de gramática para acomodar mejor los puntos neuráticos. También implementando el análisis se encontraron los siguientes problemas.
1.- Se podía generar arreglos de manera infinita ya que estaban al nivel de varcte. Como los arreglos textuales se pueden generar con expresiones, se podía anidar arreglos textuales en arreglos textuales. Para resolver esto se reestructuro la gramática para que solo se puedan utilizar en las asignaciones, las llamadas a función y las impresiones
2.- Hay que experimentar más con la verificación de los parametros en una llamada a función. Esto hay que revisar que no rompa con el orden de las operaciones y probablemente hay que verlo mejor. En este avance no se pudo aplicar.
3.- No se sabe todavía como manejar las funciones de retorno

Actualmente el programa debe de:
- Detectar en las asignaciones que se haga la asignación correcta con respecto a el tipo de variable
- Detectar que se hagan las operaciones correctas con respecto a los tipos de los operandos en la mayoría de las operaciones
- Detectar que no haya definición multiple de variables o arreglos
- Detectar que no haya definición multiples de funciones
- Desplegar mensajes de error adecuados cuando haya errores de semantica

