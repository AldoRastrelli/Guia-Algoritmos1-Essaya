#include <stdio.h>
#include <string.h>

int main(){

    void intercalar(char cadena1[],char cadena2[]);

    intercalar("hola","mundo!");
    return 0;
}


void intercalar(char cadena1[],char cadena2[]){

    int i = 0;
    char nuevo[strlen(cadena1)+strlen(cadena2)];
    while (cadena1[i] != '\0' && cadena2[i] != '\0'){
        nuevo[2*i] = cadena1[i];
        nuevo[2*i+1] = cadena2[i];
        i++;
    }

    int j = 2*i;
    if(cadena1[i] == '\0'){
        while (cadena2[i] != '\0'){
            nuevo[j] = cadena2[i];
            i++;
            j++;
        }
    }

    if(cadena2[i] == '\0'){
        while (cadena1[i] != '\0'){
            nuevo[j] = cadena1[i];
            i++;
            j++;
        }
    }
    nuevo[j] = '\0';

    printf("%s\n",nuevo);
    return;
}