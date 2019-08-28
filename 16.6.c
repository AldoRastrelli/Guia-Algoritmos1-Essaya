#include <stdio.h>
#include <string.h>

void main(){

    const char viejo[] = "Aldana";
    char nuevo[strlen(viejo)+1];
    strcpy(nuevo,viejo);
    printf("%s\n",nuevo);
    return;
}