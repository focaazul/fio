#include <fstream>
#include <iostream>

using namespace std;
struct datos{char dia[9];float temp;};

int main(int argc, char *argv[]) {
datos *muestra;//puntero.
char dia_semana[9];
int cantidad;
float z;
cout<<"Ingrese cantidad de instancias: "<<endl;
cin>>cantidad;
muestra=new(nothrow) datos[cantidad];//creo instancias
if(!muestra)
	{
	cout<<"Finaliando, no hay memoria suficiente!"<<endl;
	return -1;
	}
cout<<"Creamos :"<<cantidad<<" de instancias:"<<endl;
ofstream fsalida("prueba.txt",ios::binary);
for(int i=0;i<cantidad;i++)
	{
	cout<<"Ingrese dia ( Lu, Ma.. Do):"<<endl;
	cin>>(muestra+i)->dia;
	fsalida.write((muestra+i)->dia,(9*(sizeof(char))));
	cout<<"Ingrese la temperatura: "<<endl;
	cin>>(muestra+i)->temp;
	fsalida.write((char*)&((muestra+i)->temp),(sizeof(float)));
	}
fsalida.close();
ifstream fentrada("prueba.txt",ios::binary);
for(int i=0;i<cantidad;i++)
{
	fentrada.read(dia_semana,(9*(sizeof(char))));
	cout<<"Dia: "<<dia_semana<<'\t';
	fentrada.read((char *)&z,sizeof(float));	
	cout<<"Temperatura: "<<z<<'\t';
}
fentrada.close();
return 0;
}
