#include <iostream>
#include <new>
using namespace std;
	
int main () {	
cout << "Tratando de obtener de memoria.... "<<endl;
//1 char son bits.
cout<<"El tamanio en bytes que solicito es:"<<10406*sizeof(char)<<endl;
try{ // intento crear espacios dentro del bloque try
//char* p = new (nothrow) char [10406];	
//char* p2= new (nothrow) char [10400000000576]; //este va a tirar error 9 Terabytes
char* p1 = new char [10406];	
char* p2= new char [10400000000576]; //este va a tirar error 9 Terabytes
if (!p1){
    throw -1;
	//cout<<"No hay espacio en memoria para p2"<<endl;
    }
else{
    cout << "Espacio para p Exitoso!!\n";
    delete[] p1;
    }
if (!p2){
	throw -1;
	//cout<<"No hay espacio en memoria para p2"<<endl;
}
else{
	cout << "Espacio para p2 Exitoso!!\n";
	delete[] p2;
}
}
catch(int x)
{
    cout << "Fallo, no puedo obtener espacio en memoria!, error del tipo:"<<x;
}

	
return 0;
}
 
