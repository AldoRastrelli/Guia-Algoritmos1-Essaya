#include <stdio.h>

int _long(int i, char s[]);

int main(){

    int i = 0;
    char s[] = "hola que tal";
    printf("%d\n",_long(i,s));
    return 0;
    
}

int _long(int i, char s[]){
    
    if (s[i] != '\0'){
        i++;
        return _long(i,s);
    } return i;
    
}
