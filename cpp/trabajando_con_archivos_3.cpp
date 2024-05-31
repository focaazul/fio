#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) 
{
	cout<<" Este programa permite crea un archivo con lecturas de temperatura "<<endl;
	cout<<" humedad para distintos dÃ­as de la semana "<<endl;
	cout<<" Todo se guarda en un archivo / home / daniel / prueba . txt "<<endl;
	cout<<" ctrl + D finaliza el programa . "<<endl;
	int i=1; char dia [11];float temp,humedad; // Variables usadas para pasar datos al flujo
	ofstream flujo("/home/daniel/prueba.txt" , ios::out | ios::ate) ; // AÃ±ade al   final
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
	ifstream flujo_entrada( "/home/daniel/prueba.txt"); // ios :: in implicito !!
	if(!flujo_entrada) // Controlo que se pueda crear el flujo y asociar al archivo
	{ cout<<"Error no se puede abrir archivo .Finalizando" ; cin.get(); return -1;}
	cout<<endl<<" Flujo de entrada abierto correctamente !.!. "<<endl;
	cout<<" Nro . "<<'\t'<<" Dia " <<'\t'<<" Temp . " <<'\t'<<" Humedad "<<endl; 
	while (!flujo_entrada.eof()) 
		{
		flujo_entrada>>i>>dia>>temp>>humedad; 
		cout<<i<<'\t'<< dia<<'\t'<<temp<<'\t'<<humedad<<endl; 
		cin.get();
		}
	flujo_entrada.close();
	if(!flujo_entrada.is_open())cout<<"Flujo de Entrada:cerrado"<<endl;
	cout<<"Finalizando el programa..";
	return 0; 
}
