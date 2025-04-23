// Ejemplo de nothrow
#include <iostream>
#include <new>
using namespace std;
int main () {
cout << "Tratando de obtener 1 MB de memoria.... ";
char* p = new (nothrow) char [1048576]; //mucho espacio!!
if (!p) {             // Si el puntero es NULO no hay espacio en memoria
cout << "Fallo, no puedo obtener espacio en memoria!\n";
}
else {
cout << "Exitoso!!\n";
    delete[] p;
}
return 0;
}
