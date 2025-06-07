/*
 * Autor: Daniel Refosco
 * Fecha: 06/06/2025
 * Descripción: Este programa recibe desde la linea de comandos como argumento un nombre
 * y crea un archivo con ese nombre y guarda 12345678 en el archivo.
 */              

#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char *argv[]) {
	if (argc < 2) {
		cerr << "Debe pasar un nombre de archivo como argumento." << endl;
		return -1;
	}
	cout << "Argumento recibido: " << argv[1] << endl;
	// Abrimos el archivo, crea el archivo si no existe
	ofstream archivo(argv[1], ios::app);
	if (!archivo) {
		cerr << "No se pudo crear el archivo: " << argv[1] << endl;
		return -2;
	}
	archivo << "1234";
	archivo << "5678"<<endl;
	archivo.close();
	cout << "Archivo creado exitosamente.\n";
	return 0;
}
