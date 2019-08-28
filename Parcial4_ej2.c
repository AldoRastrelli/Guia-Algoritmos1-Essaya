#include <stdio.h>
#include <string.h>

void invertir(char s[]);

int main(){

    int N = 30;
    char s[N];
    printf("Ingrese una cadena menor a %d caracteres: ", N);
    fgets(s,30,stdin);
    invertir(s);
    return 0;
}

void invertir(char s[]){
    
    int len_cad = strlen(s)-1;
    int ultimo = len_cad -1;
    int i = 0;

    for (i = 0 ; i < ultimo - i ; i++){
        char x = s[i];
        s[i] = s[ultimo-i];
        s[ultimo-i] = x;
    }
    printf("%s\n",s);
    return;
}