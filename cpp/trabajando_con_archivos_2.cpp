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
	/*Al enviar la señal de EOF con ctrl-d además de marcarse los bits eof y fail,
	también se marca el flag de error. El flujo (cin) queda bloqueado 
	reteniendo el último ingreso. Para desbloquear el flujo cin es necesario 
	limpiar las banderas y los flags de error después del ingreso de ctrl-d */
	clearerr(stdin);
	cin.clear();
	flujo.close();
	if(!flujo.is_open()) cout<<"Flujo cerrado "<<endl;
	cout<<" Finalizando el programa !! ";
	cout<<"presiones Enter para terminar...";
	cin.get();
	return 0;
}
