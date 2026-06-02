*
Este archivo es para probar el posicionamiento en un archivo usando los métodos seekg y tellg.
 
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
    }

    pos = flujo.tellg();
    cout << "Ahora la posicion de lectura es: " << pos << endl;

    flujo.get(c);

    cout << "Caracter leido: " << c << endl;

    pos = flujo.tellg();
    cout << "Ahora la posicion es: " << pos << endl;

    cout << "Presione ENTER para continuar";
    cin.get();

    cout << "\nIngrese una posicion: ";
    cin >> n;

    flujo.seekg(n);

    pos = flujo.tellg();
    cout << "Ahora la posicion es: " << pos << endl;

    flujo.get(c);

    cout << "Caracter leido en la posicion " << n
         << ": " << c << endl;

    pos = flujo.tellg();
    cout << "Ahora la posicion es: " << pos << endl;

    cin.ignore();

    cout << "\nPresione ENTER para continuar";
    cin.get();

    flujo.seekg(-1, ios::end);

    pos = flujo.tellg();
    cout << "\nPosicion antes de leer el ultimo caracter: "
         << pos << endl;

    flujo.get(c);

    cout << "Ultimo caracter del archivo: "
         << c << endl;

    pos = flujo.tellg();
    cout << "Ahora la posicion es: "
         << pos << endl;

    return 0;
}
