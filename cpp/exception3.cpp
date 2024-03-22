
#include <iostream>
#include <cmath>

using namespace std;

static const int EDOMINIO=100;
static const int ERANGO=101;
//prueba
class ErrorMat
{
public:
	ErrorMat() : motivo(0) {};
	ErrorMat(int m) : motivo(m) {};
	const char* porque() const throw();
	
private:
	int motivo;
};

const char* ErrorMat::porque() const throw()
{
	switch (motivo)
	{
	case EDOMINIO: return "Error, no se puede calcular logaritmo de valor negativo ";break;
	case ERANGO:   return "Error, no existe el logaritmo de cero ";break;
	default:       return "Error Desconocido";  //En rigor no debería ocurrir tal Excepción 
	}	
}

double logaritmo(const double n) //Función logaritmo.
{
	try {//creo el bloque try para trata si existe  exception
		if (n < 0) throw(ErrorMat(EDOMINIO) ); //si es negativo invoco exception con 
												// argumento clase ErrorMat , argumeto EDOMINIO
		if (n == 0) throw(ErrorMat(ERANGO) );//si es cero invoco exception con 
											// argumento clase ErrorMat , argumeto ERANGO
		return log(n);// si no hay excepciones calculo el log(n)
	}
	catch(ErrorMat& argumento) {//catch captura invocando a la clase ErrorMat y le pasa el argumento.
		cout << argumento.porque();// el método porque aplicado sobre el argumento 
							//explica el origen del error.
	}
	return 0;
}

int main()
{
	double r ;
	cout<<"Ingrese el valor a calcular el log en base 10: "<<endl;
	cin>>r;
	cout << "log(" << r << ") = " << logaritmo(r) << endl;//invoco a logaritmo, que tiene el manejo de excepcion
	return 0;
}
