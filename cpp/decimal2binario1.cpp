#include<iostream>
using namespace std;
int main()
{
int decimal=397;
int binario[9];// se que 2 elevado a la 9=512 > 397
// con 9 bit puedo representar el nro. 397 en binario.
for(int i=0;i<9;i++){
binario[8-i]=decimal%2;//tomo el resto de la división
//cout<<"binario["<<i<<"]="<<binario[i]<<endl;
//cout<<"binario["<<8-i<<"]="<<binario[8-i]<<endl;
decimal=decimal/2;//tomo el nuevo cociente.
//cout<<"Decimal: "<<decimal<<endl;
}
binario[9]=decimal;
//cout<<"binario[9]"<<binario[9]<<endl;
//cout<<endl<<endl;
//Esto sería lo almacenado en el Arreglo
for(int i=0; i<9;i++){
cout<<binario[i];
}
}
