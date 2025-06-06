#include <fstream>
#include <iostream>

using namespace std;
struct datos{float temp;};

int main(int argc, char *argv[]) {
datos muestra[3];
float z;
ofstream fsalida("prueba.txt",ios::binary);
for(int i=0;i<3;i++)
	{
	cout<<"Ingrese la temperatura: "<<endl;
	cin>>muestra[i].temp;
	fsalida.write((const char *)&muestra[i].temp, sizeof(float));
	}
fsalida.close();
ifstream fentrada("prueba.txt",ios::binary);
for(int i=0;i<3;i++)
{
	fentrada.read( (char *)&z,sizeof(float));
	cout<<"Temperatura: "<<z<<" ";
	}
fentrada.close();
	
	return 0;
}

