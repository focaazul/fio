/*
Este archivo es para probar el posicionamiento en un archivo usando los métodos seekp y tellp.

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
    flujo.flush(); // vuelco flujo al archivo
    cout<<"Verifique que el contenido del archivo prueba.txt tiene ZZZ al inicio."<<endl;
    cout<<"Presione ENTER para continuar"<<endl;
    cin.get();
      
    cout << "Ingrese un valor entero: ";
    cin >> n;
    flujo.seekp(n);
    flujo << "XXX";// envío XXX al flujo
    flujo.flush(); // vuelco flujo al archivo
    pos = flujo.tellp();//averiguo la posición.
    cout<<"Verifique que el contenido del archivo prueba.txt tiene XXX en la posición:" << n << " ingresada."<<endl;
    cout << "Ahora la posicion es: " << pos << endl;
        
    flujo.seekp(0, ios::end);
    flujo << "YYY"; // envío YYY al flujo
    flujo.flush();// vuelco flujo al archivo
	cout<<"Verifique que el contenido del archivo prueba.txt tiene YYY al final del archivo."<<endl;
    cin.get();

    return 0;
}
