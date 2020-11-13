/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
	char name[20];
	
	printf("What is your name?");
	
	fgets(name,20,stdin);
	
	printf("Hello %s", name);
	
	return 0;
}