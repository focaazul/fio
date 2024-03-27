#include <iostream>
#include <fstream>
using namespace std;
int suma(const char* filename);
int main(){
//vamos a acceder a la funcion que suma
cout<<"La suma de los nros. del archivo es:"<<suma("terminos_fibonacci.txt");
return 0;
}

int suma(const char* filename)
{
ifstream *fichero = new ifstream(filename);
int sum = 0, i;
while (*fichero >> i)//voy sumando los nros. del archivo.
sum += i;
delete fichero;//elimino el objeto.
return sum;//regreso la suma.
}
