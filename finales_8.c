#include <stdio.h>
#include <string.h>

int main(){

    void imprimir_ordenados(char cadena1[], char cadena2[]);

    char cadena1[5] = "aabxz";
    char cadena2[6] = "bcddyy";

    imprimir_ordenados(cadena1,cadena2);
    return 0;
}

void imprimir_ordenados(char cadena1[], char cadena2[]){

    int len1 = strlen(cadena1);
    int len2 = strlen(cadena2);

    int j = 0;
    int i = 0;
    int indice = 0;
    char nuevo[len1+len2];

    while (cadena1[i]!= '\0' && cadena2[j] != '\0'){
        if(cadena1[i] < cadena2[j]){
            nuevo[indice] = cadena1[i];
            i++;
            indice++;
        } else {
            nuevo[indice] = cadena2[j];
            j++;
            indice++;
        }
    }

    if (cadena1[i] == '\0'){
        while (cadena2[j] != '\0'){
            nuevo[indice] = cadena2[j];
            j++;
            indice++;
        }
    } else {
        while (cadena2[j] != '\0'){
            nuevo[indice] = cadena1[i];
            i++;
            indice++;
        }
    }
    nuevo[indice] = '\0';
    printf("%s\n",nuevo);
    return;
}