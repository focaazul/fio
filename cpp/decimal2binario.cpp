#include<iostream>
using namespace std;
int main()
{
int decimal=397;
int binario[9];// se que 2 elevado a la 9=512 > 397
// con 9 bit puedo representar el nro. 397 en binario.
int temp;

for(int i=0;i<10;i++){
binario[i]=decimal%2;//tomo el resto de la división
decimal=decimal/2;//tomo el nuevo cociente.
}
//Esto sería lo almacenado en el Arreglo
for(int i=0; i<9;i++){
cout<<binario[i];
}
cout<<endl<<" vemos que falta invertir el orden"<<endl;
//Si verificamos veremos que esta invertido, vamos a corregir.
//roto en el mismo arreglo,
for(int i=0; i<5;i++){
temp=binario[i];
binario[i]=binario[8-i];//roto los valores
binario[8-i]=temp;
}
//Esto sería lo almacenado en el Arreglo

for(int i=0; i<10;i++){
cout<<binario[i];
}
cout<<endl<<" luego de invertir el orden .."<<endl;
}
