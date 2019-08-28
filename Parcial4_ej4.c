/*7) Escribir en C una programa que le solicite un n ́umero entero al usuario y muestre por
pantalla si el n ́umero ingresado es un n ́umero primo o no.*/

#include <stdio.h>
#include <math.h>

void es_primo(int n);

int main(){

    char input[10];
    printf("Ingrese un número entero: ");
    fgets(input,10,stdin);

    int numero = atoi(input);
    es_primo(numero);

    return 0;
}

void es_primo(int n){
    
    int i;
    for (i = 2; i<n; i++){
        float resto = n%i;
        if (resto == 0){
            printf("No es primo.\n");
            return;
        }
    }
    printf("Es primo\n");
}