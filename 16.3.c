#include <stdio.h>

float promedio(int lista[],int n);

float main(){
    int lista[] = {1,2,3,4};
    int n = 4;
    return promedio(lista,n);
}

float promedio(int lista[], int n){
    
    float suma = 0;

    for (int i = 0; i < n; i++){
        suma += lista[i];
    }
    float promedio = suma / (n);
    printf("promedio: %f\n",promedio);
    return promedio;
}

