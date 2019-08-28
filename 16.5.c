#include <stdio.h>
#include <string.h>

void invertir(char s[]);

int main(){
    char s[10] = "holas";
    invertir(s);
    return 0;
}

void invertir(char s[]){ //inplace

    int i = strlen(s);
    int ultimo = i -1;
    while (i >1){
        char x = s[ultimo - i];
        s[ultimo-i] = s[i];
        s[i] = x;
        i--;
    } s[ultimo+1] = '\0';
    printf("%s\n",s);
    return;
}