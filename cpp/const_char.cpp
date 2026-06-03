#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char *argv[]) 
{
const char X ='A'; //X es un Valor constante...no puede ser modificado
X='D';// El compilador acusaría error: assignment of read-only varaible ’X’
const char Z; //Error NO inicializo la constante!!
char Y = 'B'; // Y es Variable, si puede ser modificado.
Y='C'; //ok.
return 0;
}
