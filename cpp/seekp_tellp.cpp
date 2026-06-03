/*
* Archivo   : seekp_tellp.cpp
* Autor     : Daniel Refosco
* Fecha     : 02/06/2026
* Descripción:
*   Ejemplo de uso de las funciones tellp() y seekp() para consultar
*   y modificar la posición del cursor de escritura en un archivo.
*/
#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char *argv[]) {
    int n;
    long pos;
    cout << "Este programa busca mostrar el uso de: seekp(), tellp()" << endl;
    fstream flujo("./prueba.txt", ios::in | ios::out);
    if (!flujo) {
        cout << "Error no se puede abrir archivo. Finalizando";
        cin.get();
        return -1;
    }
    pos = flujo.tellp();//averiguo la posición.
    cout << "Ahora la posicion es: " << pos << endl;
    flujo << "ZZZ"; // envío ZZZ al flujo
    flujo.flush(); // vuelco flujo al archivo tres Zs
    cout<<"Verifique que el contenido del archivo prueba.txt tiene ZZZ al inicio."<<endl;
    cout<<"Presione ENTER para continuar"<<endl;
    cin.get();//espero que presione una tecla
    cout << "Ingrese un valor entero: ";
    cin >> n; //ingreso 10 
    flujo.seekp(n);//me paro para escribir en la posición 10
    flujo << "XXX";// envío XXX al flujo 
    flujo.flush(); // vuelco flujo al archivo
    pos = flujo.tellp();//averiguo la posición, sería la 13 (10+3)
    cout<<"Verifique que el contenido del archivo prueba.txt tiene XXX en la posición:" << n << " ingresada."<<endl;
    cout << "Ahora la posicion es: " << pos << endl;    
    flujo.seekp(0, ios::end);//Me paro en el final del archivo
    flujo << "YYY"; // envío YYY al flujo
    flujo.flush();// vuelco flujo al archivo
	cout<<"Verifique que el contenido del archivo prueba.txt tiene YYY al final del archivo."<<endl;
    cin.get();
    return 0;
}
