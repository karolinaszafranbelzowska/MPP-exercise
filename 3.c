#include <stdio.h>
#include <string.h>

int main()
{
    char* name[20]

    printf("What is your name?");

    gets(name);

    if (strcmp(name, "Alice") == 0)
    {
        printf("Hello %s", name);
    } else
    {
        printf("Hello stranger!");
    }
    
    return 0;

}