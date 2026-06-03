/*
* Archivo   : seekg_tellg.cpp
* Autor     : Daniel Refosco
* Fecha     : 02/06/2026
* Descripción:
*   Ejemplo de uso de las funciones tellg() y seekg() para consultar
*   y modificar la posición del cursor delectura en un archivo.
 
*/
#include <iostream>
#include <fstream>

using namespace std;
int main()
{
    int n;
    long pos;
    char c;
    cout << "Este programa muestra el uso de seekg() y tellg()" << endl;
    fstream flujo("./prueba.txt", ios::in);
    if (!flujo)
    {
        cout << "Error al abrir el archivo" << endl;
        return -1;
    }//Si puedo crear el flujo continuo.
    pos = flujo.tellg();//averiguo donde esta el cursor de lectura es la cero 0
    cout << "Ahora la posicion de lectura es: " << pos << endl; // la cero donde está la 1er Z.
    flujo.get(c);//Obtengo al caracter en el que está el cursor de lectura.
    cout << "Caracter leido: " << c << endl;//muestro el caracter
    pos = flujo.tellg();//cargo en pos la ubicación actual del cursor de lectura sería la 1
    cout << "Ahora la posicion es: " << pos << endl;//muestro la posición, una mas por que escribí un carcter
    cout << "Presione ENTER para continuar";
    cin.get();
    cout << "\nIngrese una posicion: ";
    cin >> n;//ingreso 10 por ejemplo
    flujo.seekg(n);
    pos = flujo.tellg();
    cout << "Ahora la posicion es: " << pos << endl; 
    flujo.get(c); // obtengo una X de esa posición
    cout << "Caracter leido en la posicion " << n << ": " << c << endl;
    pos = flujo.tellg();//ahora está en la posiciṕon 11
    cout << "Ahora la posicion es: " << pos << endl;
    cin.ignore();
    cout << "\nPresione ENTER para continuar";
    cin.get();
    flujo.seekg(-1, ios::end);//Ubicá el cursor de lectura 1 byte antes del final del archivo.
    // https://en.cppreference.com/cpp/io/basic_istream/seekg 
    pos = flujo.tellg();
    cout << "\nPosicion antes de leer el ultimo caracter: " << pos << endl;
    flujo.get(c);//obtengo el caracter que de esa posición
    cout << "Ultimo caracter del archivo: "<< c << endl;
    pos = flujo.tellg();
    cout << "Ahora la posicion es: "<< pos << endl;
    return 0;
}
