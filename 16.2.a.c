#include <stdio.h>

int main(){

    int n = 5;
    int factorial = 1;
    for (int i = 0; i<n; i++){
        factorial = factorial * (n-i);
    }
    printf("Factorial de %d es %d\n",n,factorial);
    return factorial;
}