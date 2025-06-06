/*Este código asigna como nombre de un archivo
al argumento pasado  al ejecutar en la terminal */

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) 
{
cout<<"cantidad de argumentos pasados:"<<argc<<endl;
for(int i=0;i<argc;i++) cout<<"Argumento :"<<i<<" es : "<<argv[i]<<endl;
fstream flujo(argv[1], ios::app);
flujo<<"Hola 1 "<<endl;
flujo<<"Mundo 1 "<<endl;
flujo.close();
return 0;
}
