#include<iostream>
using namespace std;
int main()
{
int decimal=12345678;
int binario[9];

for(int i=0;i<9;i++){
binario[i]=decimal%2;//tomo el resto de la división
decimal=decimal/2;//tomo el nuevo cociente.
}

for(int i=0; i<9;i++){
cout<<binario[i];
}
