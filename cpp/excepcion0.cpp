#include <iostream>
using namespace std;

int main(int argc, char *argv[]) 
{
	float a,b;
	cout<<"Ingrese un valor para a: "<<endl;
	cin>>a;
	cout<<"Ingrese un valor para b: "<<endl;
	cin>>b;
	cout<<"Vamos a calcular el cociente de :"<<a<<" sobre "<<b<<endl;
	
	try //voy a tratar
	{
		if(b==0) throw -1;//si b es cero genero una excepción ya que no puedo dividir por cero.!!
		cout<<a/b;//si b no es cero ejecuto esta línea
	}
	catch( int x)
	{
		cout<<"No se puede dividir por cero, nro error: "<<x;
	}
	return 0;
}


