#include <iostream>
using namespace std;

float division(int a, int t) {
	if (t == 0) {
		throw "Error!!. Ud. está intentando dividir por cero ";//esgte texto paso a cathc como argumento.
	}
	return (a / t);
}
int main() {
	int x,y;
	float z;
	cout<<"Ingrese numerador:"<<endl;
	cin>>x;
	cout<<"Ingrese denominador:"<<endl;
	cin>>y;
	try {
		z = division(x, y);//llamo a la función.
		cout << z << endl;//muestro lo que regresa la función.
	} catch (const char* msg) { //thow, tiene como argumento un texto, esto se pasa a catch
		cerr <<"línea 21 con cerr dice:"<< msg << endl; //esta línea muestra el mensaje por pantalla
		cout<<"línea 22 con cout dice:"<< msg << endl; //esta línea muestra el mensaje por pantalla
	}
	return 0;
}
