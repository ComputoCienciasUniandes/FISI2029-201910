# Ejercicio 11
## Intrucciones.
Guarde las respuestas a cada punto en un archivo separado con el nombre indicadoen el respectivo punto. La solución debe estar en su repositorío. y a cada punto se debe tener su respectivo commit.
## Ejerciccios
--------------------------
1. Escriba un programa que le pida al usuario el radio de un círculo y luego imprima el diámetro, el prímetro y el área correspondientes. LLame a este programa 1.cpp.
2. Escriba un programa que lea tres números enteros e indique si esos números pueden representar los lados de un triángulo rectángulo. Use como caso de prueba 3,4,5 (si) y 3,4,6 (no). Guarde el programa en el archivo 2.cpp
3. Qué está mal con los siguietes códigos?
(guarde sus respuestas en el archivo 3.txt, numerándolas de acuerdo al ejemplo)
  1.
  ``` c++
  cin << cout;
  ```
  2.
  ``` c++
  if(x=0) cout << x << " =0\n"
  else cout << x << " != 0 \n"
  ```
  3.
  ``` c++
  #include <iostream>
  int main(void)
  {
    const double PI;
    int n;
    PI=3.14159265358979;
    n=22;
  }
  ```
  4.
  ``` c++
  int count;
  while(count<100)
  cout<<count;}
  ```
  5.
  ``` c++
  int a,b;
  int sum=a+b;
  cout<<"Enter two numbers to add";
  cin>>b;
  cout<<"The sum is "<<sum;
  ```
  6.
  ``` c++
  int array[10];
  for(int x=1; x<=10;x++)
  cout<<array[x]
  ```
  7.
  ``` c++
  double half = 1/2;
  ```
4. __(Genio de Facebook)__, cúal es el resultado de las siguientes expresiones en C++? (Responda a este ejercicio en un archivo con el nombre 4.txt)
  1. 8*9+2
  2. 6*3/4
  3. 3/4*6
  4. 6.0*3/4
  5. 15%4*6+8/3
## Bono
5. Haga su propia implementación de la función ``sin`` esta función ha de tener las siguientes caracteristicas. ( llame a su solución 5.cpp)
  1. Debe ser periodica, es decir:
    <img src="http://bit.ly/2D1dBSb" align="center" border="0" alt="\sin(x)=\sin(x+2n\pi)" width="178" height="18" />
    [imagen](http://bit.ly/2D1dBSb)
  2. Debe tener una precición de mínimo <img src="http://www.sciweavers.org/tex2img.php?eq=10%5E%7B-3%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="10^{-3}" width="43" height="18" />, con respecto a el valor de la librería math
  3. El programa usará una función que se llamará ``my_sin`` y al ejecutarse esté pedira al usuario el valor de x (en grados) para el cual se quiere calcular el seno y el programa debe transformar los grados a radianes y así calcular (En general se pedirá un float).
