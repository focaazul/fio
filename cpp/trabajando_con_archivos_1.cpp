#include <iostream>
#include <fstream>
using namespace std;
/*
Escribir un programa que permita presentar un menÃº como el siguiente:

1)Crear un flujo asociado a prueba.txt
2)Agregar contenido a un archivo al final
3)Cerrar un flujo asociado a prueba.txt
4)Ver si el flujo asociado a prueba.txt esta abierto.
5)Ver si el flujo asociado a prueba.txt esta cerrado.
6)Mostrar el contenido del archivo.
7)Finalizar

*/

int main(int argc, char **argv)
{
	const int ESC=27;
	bool bandera=true;
	int op;
	char algo[20];
	ofstream ingreso_datos;
	ifstream visor;
	
	do{
		cout<<"-----------ESTO ES UN MENU-----------"<<endl<<endl;
		cout<<"1.- Crear un flujo asociado a prueba.txt"<<endl<<"2.- Agregar contenido a un archivo al final"<<endl<<"3.- Cerrar un flujo asociado a prueba.txt"<<endl<<"4.- Ver si el flujo asociado a prueba.txt esta abierto"<<endl;
		cout<<"5.- Ver si el flujo asociado a prueba.txt esta cerrado"<<endl<<"6.- Mostrar el contenido del archivo"<<endl<<"7.- Finalizar"<<endl;
		cout<<endl<<"--------------------------------------------------------------"<<endl;
		cout<<endl<<"Ingrese su opcion: ";
		cin>>op;
		switch(op){
		case 1:{
			ingreso_datos.open("prueba.txt",ios::out | ios::ate);	//hacer esto es lo mismo que fstream visor("prueba.txt") --> esto es asociar el flujo a un archivo de forma implísita
			break;
			}
		case 2:{
			cout<<endl<<"Ingrese algo: "<<endl;
			while(cin>>algo){
				ingreso_datos<<algo<<endl;
				//cout<<""
			}
			//Al enviar la señal de EOF con ctrl-d además de marcarse los bits eof y fail, también se marca el flag de error. 
			//El flujo (cin) queda bloqueado reteniendo el último ingreso. 
			//Para desbloquear el flujo cin es necesario limpiar las banderas y los flags de error después del ingreso de ctrl-d:
			clearerr(stdin);
			cin.clear();
			cin.ignore(1000);
			break;
			}
		case 3:
			ingreso_datos.close();		//cierro el flujo
			break;
		case 4:
			if (ingreso_datos.is_open()) cout<<endl<<"Archivo abierto"<<endl;
			break;
		case 5:
			if (ingreso_datos.is_open()==0) cout<<endl<<"Archivo Cerrado"<<endl;
			break;
		case 6:
			visor.open("prueba.txt");	//abro otro flujo, pero sólo para que salgan datos
			cout<<endl<<"----------MOSTRANDO CONTENIDO----------"<<endl;
			while(visor>>algo){
				cout<<"\t"<<algo<<endl;
			}
			cout<<endl;
			visor.close();
			break;
		case 7:
			bandera=false;
			if (!visor.is_open()) visor.close();
			if (!ingreso_datos.is_open()) ingreso_datos.close();
			break;
		default:
			cout<<endl<<"INGRESO NO VALIDO, REINTENTE"<<endl;
			break;
		}
	}while(bandera);
	return 0;
}

