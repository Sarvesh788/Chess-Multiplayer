#include <stdio.h>

int main()
{
    int a = 50;
    switch(a)
    {
        case 49: a++; break;
        default: a=45; break;
        case 50: a--; break;
        case 51: a= a + 1; break;
    }
    printf("%d", a);
}