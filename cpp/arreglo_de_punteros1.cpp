#include <iostream>
using namespace std;
int main(int argc, char *argv[]) {
    float *pa,*pi;//declaro puntero a float
    cout<<sizeof(float)<<endl;//vero el tamaño de float en bytes
    pi=pa=new float[5];//con new reservo 5 espacios consecutivos de memoria
                    // para almacenar direcciones de memoria
    //obtengo una dirección en pa, puntero al primer elemento del arreglo!!
    for(int i=0;i<5;i++){cin>>*pa;pa++;}//cargo valores pero usando punteros !!
    pa=pi; //para regresar a la posición 0 del arreglo
    for(int i=0;i<5;i++)cout<<pa[i]<<"\t"<<&pa[i]<<endl;//muestro lo almacenado
    return 0;
}
