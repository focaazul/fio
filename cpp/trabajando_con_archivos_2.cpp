#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	cout<<" Este programa permite crea un archivo con lecturas de temperatura "<<endl;
	cout<<" humedad para distintos días de la semana "<<endl;
	cout<<" Todo se guarda en un archivo / home / daniel / prueba . txt "<<endl;
	cout<<" ctrl + D finaliza el programa . "<<endl;
	int i=1; char dia [11];float temp,humedad; // Variables usadas para pasar datos al flujo
	ofstream flujo("/home/daniel/prueba.txt" , ios::out | ios::ate) ; // Añade al   final
	// El objeto flujo es abierto implicitamente .
	if (!flujo) // Controlo que se pueda crear el flujo y asociar al archivo
	{cout<<" Error no se puede abrir archivo . Finalizando " ; cin . get ();return -1;}
	cout<<"Ingrese : Dia y luego Temperatura y Humedad dejando un espacio entre  cada campo " <<endl;
	while (cin>>dia>>temp>>humedad){flujo<<i<<" "<<dia<<" "<<temp<<" "<<humedad<<endl; i++;}
	clearerr(stdin);
	cin.clear();
	flujo.close();
	if(!flujo.is_open()) cout<<"Flujo cerrado "<<endl;
	cout<<" Finalizando el programa !! ";
	cout<<"presiones Enter para terminar...";
	cin.get();
	return 0;
}
