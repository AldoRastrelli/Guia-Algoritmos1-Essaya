/*6) Escribir en C un programa que pida al usuario un valor m ́ınimo, un valor m ́aximo y un
n ́umero n, e imprima una tabla con los cuadrados de los n ́umeros entre m ́ınimo y m ́aximo cada
n n ́umeros. Por ejemplo (m ́ınimo = 0, m ́aximo = 17, n = 5) debe mostrar:
0 0
5 25
10 100
15 225*/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void cuadrados(int min, int max, int salto);

int main(){

    char min[5];
    char max[5];
    char salto[5];
    printf("Ingrese un mínimo: ");
    fgets(min,5,stdin);
    printf("Ingrese un máximo: ");
    fgets(max,5,stdin);
    printf("Ingrese el salto: ");
    fgets(salto,5,stdin);

    int min_i = atoi(min);
    int max_i = atoi(max);
    int salto_i = atoi(salto);

    cuadrados(min_i,max_i,salto_i);
    return 0;
}

void cuadrados(int min, int max, int salto){

    int num = min;
    while (num < max){
        
        int cuadrado = pow (num,2);

        printf("%d  %d\n", num, cuadrado);
        num += salto;
    }
    return;
}