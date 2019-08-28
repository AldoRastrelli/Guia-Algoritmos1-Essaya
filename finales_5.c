#include <stdio.h>

int main(){

    

    int lista1[6] = {0,3,5,8,11,20};
    int lista2[4] = {1,2,9,12};
    int largo1 = 6;
    int largo2 = 4;
    
    void imprimir_ordenados (int lista1[], int longitud1, int lista2[],int longitud2);
    imprimir_ordenados(lista1,largo1,lista2,largo2);
    return 0;
}

void imprimir_ordenados (int lista1[],int longitud1, int lista2[],int longitud2){

    int minimo;
    if (longitud1>longitud2){
        minimo = longitud2;
    } else {
        minimo = longitud1;
    }
    
    int j = 0;
    int i = 0;
    
    while (j<minimo || i<minimo){

        if (lista1[i] < lista2[j]){
            printf("%d\n",lista1[i]);
            i++;
        } else {
            printf("%d\n",lista2[j]);
            j++;
        }
    }

    if (minimo == longitud1){
        while (j<longitud2) {
            printf("%d\n",lista2[j]);
            j++;
        }
    } else {
        while (i<longitud1) {
            printf("%d\n",lista1[i]);
            i++;
        }
    }
    return;
}