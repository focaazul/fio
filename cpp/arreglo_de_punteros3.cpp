#include <iostream>
using namespace std;
int main(int argc, char *argv[]){
    float *px;
    px=new float[5];//Declaro arreglo de punteros CONSECUTIVOS
    float *pa[5];//Declaro arreglo de punteros <-Esto es nuevo!!
    cout<<sizeof(float)<<endl;
    //Espacios NO consecutivos ( cada vez que ejecuto new) .
    for(int i=0;i<5;i++){
        pa[i]=new float;//dinámicamente resevo UN espacio en memoria.
        cin>>*pa[i];//cada puntero ahora apunta al dato ingresado:inicializo
    }
    for(int i=0;i<5;i++)cout<<*pa[i]<<" "<<pa[i]<<endl;//Espacios consecutivos.
    for(int i=0;i<5;i++)
        cin>>*(px+i);//cada puntero ahora apunta al dato ingresado
    for(int i=0;i<5;i++)cout<<*(px+i)<<" "<<(px+i)<<endl;
    return 0;
}
