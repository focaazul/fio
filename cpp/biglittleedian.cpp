#include <iostream>

using namespace std;

int main(int argc, char *argv[]) 
{
    unsigned int num = 0x1;// declaro entero sin signo 
    cout<<"El tamnio de num es: "<<sizeof(num)<<" bytes"<<endl;
    // num sería: 0000 0000 0000 0001 (Big Endian) ó 0001 0000 0000 0000 (Little Endian)?
    char *ptr = (char*)&num;// tomo la dirección de num (&num), y asigno a un puntero a un char (char*)
    //notar que el puntero apunta al byte mas bajo de los 4 de num
    if (*ptr == 1) {//Si el valor el 1er Byte es 1 =>el LSB está en el primer byte "0001" 0000 0000 0000
        cout << "El sistema es Little Endian" << endl;
    } else {//Si el valor del 1er Byte NO es 1 => el MSB está en el ultimo byte "0000" 0000 0000 0001
        cout << "El sistema es Big Endian" << endl;
    }

    return 0;
}
