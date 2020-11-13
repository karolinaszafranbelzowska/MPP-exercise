/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <stdio.h>
#include <string.h>


int main()
{
    char* name;

    printf("What is your name?");

    //fgets(name,stdin);
    gets(name);

// strcmp ->string comparison
    if((strcmp(name, "Alice")==0) || (strcmp(name, "Bob")==0))
    {
        printf("Hello %s", name);
    } else
    {
        printf("Hello lowly peasants!");
    }

    return 0;
}