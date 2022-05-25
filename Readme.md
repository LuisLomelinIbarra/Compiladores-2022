# Avance 6

Ya se empezo la máquina virtual y ya funciona leyendo los cuadruplos de expresiones, el estatuto de imprimir y con las funciones definidas por el usuario (incluyendo recursion). En esta entrega me di cuenta de varios errores en la generación de cuarduplos, especificamente en el estatuto de return estaba faltando agregar el cuadruplo de enfunc para regresar a la memoria anterior. Igual mi lógica de saltos en mi for me llevaba a contar uno ciclo demás lo cual tuve que arreglar


El avance de ahora debe de:
- El compilador debe de generar un archivo json con los cuadruplos, la tabla de funciones y las constantes.
- La máquina virtual debe de leer el json y ejecutar el código en el.

COSAS QUE CAMBIAR/ARREGLAR:
- Formas de manejar los arreglos como parametros
- Terminar bien arreglos.
