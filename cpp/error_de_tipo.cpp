#include <iostream>
using namespace std;

int main () {
	int x;
    cin>>x;//en x se almacena todo hasta el Enter.
    while (!(cin.good()))
    {
		
		cout<<"Ud. NO ingresó un numeros!!. Reingrese: ";
		cin.clear();
		cin.ignore();//limpio el buffer para que no enter en bucle.
		cin>>x;
    
    }
  cout<<"Ud. ingreso el siguiente numero: "<<x;
  
  return 0;
}
