#include <iostream>
#define max_size 50 // tamanio maximo de caracteres basura

using namespace std;

int main () {
	float x;
	char basura[max_size];
    cin>>x;
    while (!(cin.good()))
    {
		cout<<"Ud. NO ingresó un numeros!!. Reingrese: ";
		cin.clear();// reseteo el bit de error.
		cin.getline(basura,max_size);//leo el contenido de buffer  max_size  de caracteres
		cin>>x;
    
    }
  cout<<"Ud. ingreso el siguiente numero: "<<x;
  
  return 0;
}
