	
#include <iostream>
#include <string> //librería que maneja tipo de dato string.
	 
using namespace std;

int main()
{	int posicion;
	string txt = "Hola";//defino un tipo de dato string que maneja la clase string.
	cout<<"Ingrese un entero: "<<endl;
	cin>>posicion;
	try {
		cout <<"el caracter en la posición " << posicion<< " es: "<< endl;
		cout<< txt.at(posicion) << endl;////muestro caracter de txt ubicado en la posición x 
	}
	catch(exception& argumento) {
		cout<<"mensaje que genera la excepcion: "<<endl;
		cout << argumento.what() << endl; //arguemnto.what retorna un puntero al texto informativo
	}
	cin.get();
	return 0;
}
