Ejercicio 12
============

### Compilacion, precompilacion, linkers e impresion en la salida estandar

1. Cree un programa en ``c++`` que reciba dentro de la función main un argumento de tipo  ``void``, el programa que debe hacer debe incluir la librería ``iostream`` y ``cmath`` para que el numero pi, y el coseno de pi.

  - Una vez tenga su programa, precompile el programa y cuente el número de lineas que la precompilación arroja a esto llamelo 1_a.cpp y el output llamelo 1_a.txt. si no recuerda como precompilar, corra con la bandera -E, es decir
  ``` bash
      g++ -E 1_a.cpp
  ```
  - Ahora imprima lo entregado por el output y mande esto a un archivo llamado 1_b.txt, auna vez hecho esto, ahora fije la precisión de la salida estandar en 16 cifras significativas y con notación cientifica, esto adjuntelo a la parte inferior del archivo 1_b.txt, este codigo debe llamarse 1_b.cpp. Para fijar la precisión utilice:
  ```c++
      std::cout.precision(16); // fija la precision en 16 cifras significativas
      std::cout.setf(std::ios::scientific); // hace que la impresión sea con notacion cientifica
  ```
  - haga el mismo ejercicio anterior para que se imprima exactamente lo mismo que en la parte anterior (misma precision y misma notacion) pero esta vez haga uso de la función ``prinf``, llame a esto 1_c.cpp, lo que debe imprimir es una variable declarada de tipo entero fuera del main como una constante. La función ``prinf`` recibe directamente los parámetros a imprimir, por ejemplo si se quiere imprimir un entero long que ocupe 10 espacios en la pantalla con presicion de 5 cifras y con notacion cientifica, se utlizaría
  ```c++
      std::prinf("%10.5le",var_imprimir)
  ```
  Así de esta forma el valor de % se remplaza por el de var_imprimir, se fijan los 10 espacios, (.5) se refiere a la precision, ``l`` dice que es un entero de tipo long y ``e`` que se imprima con notacion cientifica, vea el [enlace](http://www.cplusplus.com/reference/cstdio/printf/).

  - Compile cualquiera de los codigos anteriores haciendo uso de la bandera -c ( esta bandera es utilizada para desligar el compilador del linker), vea ahora los archivos que están en su directorio e intente visualizar ese nuevo archivo, imprima esto a un archivo que se llame 1_d.cpp, luego compile el archivo que aparecio de forma normal con el compilador ``g++ nuevoarchivo`` y ejecute la salida y observe que ocurre, comente esto en un archivo que se llamará 1_d_2.txt.

  - Ahora tome el programa de c++ 1_b.cpp y agreguele una linea ara que se imprima a la salida estandar del error, para esto agreguele
  ```c++
    std::cerr<<" El ensaje que usted quiera poner"<<std::endl;
  ```
  luego compile y corra el programa (que se llamará 1_std_err.cpp) y mande la salida a un archivo que se llama 1_std_err.txt, luego corra nuevamente el ejecutable seguido de un espacio y el numero 1 a un archivo que se llamará 1_std.txt y vea si se imprime algo en la consola, luego haga lo mismo pero con el nuemro 2 a un archivo que se llamará 2_err.txt y vea que se imprime. Comente dentro de cada archivo que fue lo que se observó que se imprimió.

### Memoria dinámica (Stack and Heap)

En algunas ocaciones nos enfretamos a problemas que requieren guardar datos de un tamaño desconocido. Para esto se necesita hacer uso de dos recursos existentes en la memoria, lo cual es el Heap y el Stack, ambas son una región de memoria en donde se puede almacenar elementos, no obstante, el Heap resulta ser mucha más grande que el Stack y por ende resulta util aprender a utilizar esto.

2. Haga un codigo en c++ (llamelo 2.cpp) en donde pida memoria de forma "convencional", es decir pida un arreglo primitivo de numeros dobles
``` c++
    double array[size];
```
fije el tamaño del arreglo en 10 y observe luego llene el arreglo con su respetivo indice es decir
``` c++
    for(int i=0;i<=size;i++)
    {
      array[i]=i;
    }
```
claramente el codigo anterior tiene un error (¿por qué?), de igual forma compile y ejecutelo. Observe que ocurre al ejecutar el programa, seguido a esto compile nuevamente el codigo haciendo uso de la bandera ``-fsanitize=address`` y ejecute nuevamente el codigo, qué aparece ahora en la salida? (comente lo que observo para ambos casos en un archivo que se llamará 2.txt)
3. Ingrese a la siguiente [pagina](http://pythontutor.com/cpp.html#mode=edit) para que tenga una idea de como funciona el codigo del punto anterior, para esto copie y pegue su coddigo y luego ejecutelo dentro de la pagina.
4. Haga una modificacion al codigo en 2.cpp y no llene el arreglo, sólo pida una memoria fija, la cual usted la pude poner directamente desde el codigo o desde la terminal, en el caso de que desee pedirla desde la terminal en lugar del main recibir un argumento void, ponga la siguiente lineas
```c++
int main(int argc, char **argv)// Esta es una opcion
int main(int argc, char *argv[])//esto es otra opcion
```
fije N= 10E9, compile y corra, comente que ocurre. ahora compile nuevamente con la bandera ``-fsanitizer==address`` y corra, qué ocurre?, qué error arroja ahora? (los comentarios de esto deben ir en un archivo llamado 4.txt)

[codigo ejemplo](http://pythontutor.com/cpp.html#code=int%20main%28void%29%0A%7B%0A%0A%20%20const%20int%20N%20%3D%2010%3B%0A%20%20double%20*a%20%3Dnullptr%3B%0A%20%20a%20%3D%20new%20double%20%5BN%5D%3B%0A%20%20for%28int%20i%20%3D%200%3B%20i%3CN%3Bi%2B%2B%29%0A%20%20%7B%0A%20%20%20%20a%5Bi%5D%3Di%3B%0A%20%20%7D%0A%20%20double%20b%5BN%5D%3D%7B0%7D%3B%0A%20%20for%28int%20i%20%3D%200%3B%20i%3CN%3Bi%2B%2B%29%0A%20%20%7B%0A%20%20%20%20b%5Bi%5D%3Di%3B%0A%20%20%7D%0A%20%20delete%20%5B%5D%20a%3B%0A%20%20return%200%3B%0A%7D&curInstr=48&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D)
