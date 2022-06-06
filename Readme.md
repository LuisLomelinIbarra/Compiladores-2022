# IntroProg : El lenguaje éstadistico para aprender a programar

IntroProg es un lenguaje de programación diseñado para principiantes que quieran aprender a programar con lenguajes estilo C/C++ experimentando con funciones estadísticas.

### Herramientas
IntroProg se logro hacer con la auyda de las siguientes herramientas:
* Python
* Ply
* SciPy
* NumPy
* MatPlotLib

### Requerimientos

Para poder utilizar el lenguaje lo único que se requiere es tener python instalado con las librerías que se mencionaron en las herramientas.

### Como correr un programa IntroProg

Para correr tu programa IntroProg debes de primero compilarlo con el archivo de IntroProg.py que se encuentra dentro de la carpeta lexnsyn
```
py IntroProg.py camino/a/tu/archivo
```

Esto generara un archivo obj el cual la máquina virtual que esta en la carpeta de virtualmachine va a usar para ejecutar tu código

```
py itvm.py camino/a/tu/archivo/obj
```

### Como utilizar el lenguaje

Para poder utilizar el lenguaje lo primero que debes de hacer es crear un archivo itp. Este archivo deberá contener tu código fuente que vayas creando.
Los archivos itp sigen la siguiente estructura :
```

programa pelos{
    //Primero deben de ir la declaracion de variables globales
    //Luego deben de ir las declaracion de tus funciones
    //Luego va la función principal
    principal funcion{}{
        imprimir("¡¡Hola Mundo!!");
    }

}

```

Los tipos que utiliza IntroProg para sus variables son los siguientes:
* Enteros
* Flotantes
* Caracteres (char)
* Booleanos (bool)

Para la declaración de una variable basta con escribir el tipo de la variable seguido por el nombre de la variable. Este nombre puede ser cualquier combinación de letras, números y guines bajos (_) que empiezen con una letra.

```
    entero num;
    flotante num2;
    char letra;
    bool booleano1;
```

### Operaciones

Para realizar operaciones con IntroProg basta con escribirlas como si fueran operaciones matemáticas.
 ```
    // suma
    num = 1+1;
    // resta
    num = num -1;
    // multiplicacion
    num2 = num * 20;
    // Division
    num2 = num /num2;
    // Tambien se pueden usar parentesis
    num2 = (1+1)*num - num2 * num2;
    // Taqmbién puedes hacer funciones relacionales y lógicas
    booleano1 = num2 > 1 || (num2 == num && num <> 1); 
 ```

### Funciones

 Para construir funciones en IntroProg debes de seguir la siguiente estructura:

 ```
  funcion tipo nombre(parametros){
      //Declaraciones
      // Se puede dejar vacio si no se usan variables locales
    }{
        //Tu asmbroso codigo
    }
```

Recuerda que puedes tener funciones que no tengan parametros y no regresen nada

``` 
    funcion vacia hola(){}{
        imprimir("Hola!!");
    }
```

O funciones que puedan hacer operaciones y que te regresen un valor
```
    funcion entera sumaMagica(entero a, entero b){
        entero ingredienteSecreto;
    }{
        ingredienteSecreto = 1000;
        regresar a + b*ingredienteSecreto;
    }
```
Y para utilizar tus funciones solo basta con escribir un $ seguido por le nombre de tu función y sus parametros entre paréntesis

```
    $hola();
    num = $sumaMagica(1,2);
```

### Funciones especiales

IntroProg también te provee una lista de funciones que puedes utilizar para tu código
*  $leer() : Regresa la lectura capturada de consola
*  $modulo(flotante a, flotante b): Regresa el resultado de a\%b
*  $suma(flotante a[]): Suma todos los elementos de un arreglo y regresa sus resultados
*  $raiz(flotante a): Regresa el flotante resultante de la raíz de a
*  $exp(flotante a): Regresa la exponencial de e\^a
*  $elevar(flotante a, flotante b): Regresa el resultado de a\^b
*  $techo(flotante a): Regresa un flotante a redondeado para arriba
*  $piso(flotante a): Regresa un flotante a redondeado para abajo
*  $cos(flotante a): Regresa el coseno de a
*  $sen(flotante a): Regresa el seno de a
*  $tan(flotante a): Regresa la tangente de a
*  $cotan(flotante a): Regresa la cotangente de a
*  $sec(flotante a): Regresa la secante de a
*  $cosec(flotante a): Regresa la cosecante de a
*  $log(flotante a): Regresa el logaritmo natural de a
*  $minimo(flotante a[]): Regresa el valor más chico en el vector a
*  $maximo(flotante a[]): Regresa el valor máximo de a
*  $redondear(flotante a): Regresa un flotante a redondeado
*  $productoPunto(flotante a[], flotante b[]): Regresa el producto punto entre los vectores de entrada a y b
*  $media(flotante a[]): Regresa la media de a
*  $mediana(flotante a[]): regresa la mediana de a
*  $moda(flotante a[]): Regresa el elemento con la moda más alta de a
*  $varianza(a): Regresa la varianza de a
*  $percentil(flotante a[], flotante q): Regresa el valor en el que se encuentran q% de los valores en a
*  $aleatorio(flotante min, flotante max): Regresa un número flotante aleatorio entre los rangos de argumentos mínimos y máximos
*  $wilcoxon(flotante x[]): Realiza la prueba de Wilcoxon en la serie de datos en x
*  $wilcoxonComp(flotante x[], flotante y[]):Realiza la prueba de Wilcoxon se realiza la prueba sobre los datos x y y
*  $regresionSimple(flotante x[], flotante y[], flotante xi): Dado un set de x y y se usará regresión lineal simple para encontrar f(xi) y se regresara ese valor
*  $normal(flotante media, flotante desv): Regresa un número escalar que pertenezca a la distribución normal dado los parámetros
*  $poisson(flotante lambda): Regresa un número aleatorio de la distribución Poisson con la lambda dada
*  $dexponencial(flotante beta): Regresa un número aleatorio de la distribución Exponencial correspondiente a la beta (o 1/Lambda) dada
*  $dgeometrica(flotante exito): Te regresa un valor con la distribución geométrica con la probabilidad de exito dada
*  $histograma(flotante x[], flotante rango): Genera un histograma a partir de los datos en el vector de x con un rango entre los datos de rango
*  $diagramadecaja(flotante x[]): Genera un diagrama de caja y bigotes de los datos en en x
*  $grafDispersion(flotante x[], flotante y[]): Genera un gráfico de dispersión con los valores de ‘x’ y ‘y’


### Agradecimientos

Gracias a mi familia. A mi mamá y a mi hermano por apoyarme mucho durante todo este tiempo. Sin ellos realmente no sabría en donde estaría ahora.
Gracias a mis amigos. Por estar allí en los momentos buenos y malos. Por hacer la vida más interesante
Gracias a mis profesores. Por pasar su conocimiento con paciencia y entusiasmo, y por darme la oportunidad de hacer grandes cosas

Gracias