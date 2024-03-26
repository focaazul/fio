#include <iostream>
#include <stdexcept>

using namespace std;

int check_neg(int a, int b) {
	if (a < 0 || b < 0) { // Si algun argumento es negativo, llamo a una excepcion
		throw invalid_argument("Valor negativo encontrado");
	}
	else{
		cout<<"Parametros pasados: "<<a<<" y "<<b<<endl;
	}
	return 0;
}

int main() {
	int x,y;
	cout<<"Ingrese un entero: "<<endl;
	cin>>x;
	cout<<"Ingrese otro entero: "<<endl;
	cin>>y;
	try {
		check_neg(x, y);//llamo a la funcion dentro del bloque try
	} catch (const invalid_argument& e) {
		cout << "Argumento invalido!!"<<" : "<<e.what();
	}
}

