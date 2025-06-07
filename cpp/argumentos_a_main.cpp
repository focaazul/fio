/*
 * Autor: Daniel Refosco
 * Fecha: 06/06/2025
 * Descripción:Argumentos a main.
 */        

#include <iostream>
using namespace std;

/*
argc es un  entero y  contiene el numero de argumentos que se han introducido.
argv array de punteros a caracteres y almacena los valores pasados como argumentos.
*/

int main(int argc, char *argv[]) {
	cout<<"cantidad de argumentos pasados:"<<argc<<endl;
	for(int i=0;i<argc;i++)
		cout<<"Argumento :"<<i<<" es : "<<argv[i]<<endl;
	return 0;
}
