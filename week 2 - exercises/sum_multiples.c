/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <stdio.h>
#include <string.h>


int main()
{
    int n;
    int sum = 0;

    printf("Please enter a Number:" );
    scanf("%d", &n);

    for(int i = 1; i<=n; i++)
    {
        if(((i%3)==0) || ((i%5)==0))
        {
            printf("%d was added \n", i);
            sum +=i;
        }

    }
    printf("The sum of 1 to %d, was %d\n", n , sum);
    return 0;
}