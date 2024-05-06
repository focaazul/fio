#include<iostream>
using namespace std;
struct datos {float valor; datos *p_prox;};
void cargar(struct datos *&p);
void mostrar(struct datos *p); // esto muestra lo que cargo
//void liberar(struct datos *&p) esta funcion FALTA!!!
char menu(void);


int main()
{
struct datos *p_inicial=NULL;
char opc;
do
	{
	opc=menu();
	switch(opc)
		{
		case '1':
			cout<<"Cargue una instancia"<<endl;
			cargar(p_inicial);
			break;
		case '2'://muestro lo cargado.
			mostrar(p_inicial);
			break;
		case 's':
		case 'S':cout<<"Finalizando..";
			break;
		default:
			cout<<"La opcion ingresada NO es valida, reingrese."<<endl;
		}
	}while (!(opc=='s' or opc=='S'));

}


void cargar(struct datos *&p)
{
datos *p_temp;// puntero temporal
if (p==NULL)//Si es NULL => primer instancia.
	{p=new datos;// Creo la primer instancia.
	cout<<"Ingrese valor: ";
	cin>>p->valor;
	p->p_prox=NULL;}  // dejo puntero a NULL para la 1er Instancia
else
	{
	p_temp=p; //inicializo la copia local
	while (p_temp->p_prox!=NULL) //recorro hasta llegar a la ultima instancia.
		{p_temp=p_temp->p_prox;}
		p_temp->p_prox=new datos;//nueva direccion de la proxima instancia reemplaza a NULL
		p_temp=p_temp->p_prox; //me paro en la nueva instancia.
		cout<<"Ingrese valor: ";
		cin>>p_temp->valor;
		p_temp->p_prox=NULL;//pongo en NULL el puntero a prox de la ultima instancia.
	}
}


void mostrar(struct datos *p_temp)
{
if (p_temp==NULL){cout<<"No hay nada que mostar.."<<endl;return;}
int contador=1;
cout<<"Nro."<<"\t"<<"Direccion"<<"\t"<<"Valor"<<"\t"<<"Punt_prox"<<endl;
while (p_temp!=NULL){
	cout<<contador<<"\t"<< p_temp<<"\t"<<p_temp->valor<<"\t"<<p_temp->p_prox<<endl;
	p_temp=p_temp->p_prox;
	contador+=1;}
}


char menu()
{
char opc;
cout<<"Ingrese 1 para cargar, 2 para mostar, s o S para salir: "<<endl;
cin>>opc;
return opc;
}


