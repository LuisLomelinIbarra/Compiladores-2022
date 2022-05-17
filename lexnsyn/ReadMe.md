# Avance 5

Se implemento todo lo de modulos. Para cada función ahora se va guardando la cantidad de variables que se estan utilizando en ella, el cuadruplo donde inicia y si tiene retorno la dirección de la variable global de retorno. En la llamada de función se verifica que los parametros llamados sean los correctos, de ser así se genera el cuadruplo para generar la memoria y los cuadruplos para copiar los parametros a la nueva memoria. Al final se agrega el gosubfunc que apunta al inicio de la función llamada. En caso de ser función especial llama a el cuadruplo SPFUNC, indicando que es función especial.


El avance de ahora debe de:
- En el archivo de cuadruplos ahora ya debe de generar los cuadruplos correspondientes de cada función declarada (ERA y PARAMS). En caso de ser función especial llama al cuadruplo SPFUNC con el nombre de la función en vez de GOSUBFUNC.

COSAS QUE CAMBIAR/ARREGLAR:
- Una mejor manera para manejar las constantes String
- Corregir el error de la variable syntactica que permite que se pueda declarar un arreglo así [1, [1,1]]
