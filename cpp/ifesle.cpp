int main(int argc, char *argv[]) 
{
int hora;
cout<<"Ingrese la hora (enteros[0,24]:"<<endl;
cin>>hora;
if(hora<12) //es de mañana
cout<<"Buenos días...";
else if (hora<18) //estoy entre las 12 y 18
cout<<"Buenas tardes..";
else if (hora<20) //estoy entre las 18 y 20
cout<<"Buenas noches..";
else
cout<<"hora de dormir..";
return 0;
}
