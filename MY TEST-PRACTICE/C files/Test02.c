#include <stdio.h>

/**
 * main - entry point
 * ask user for input
 * must not be zero
 */

int main()
{
    int n;

    printf("Enter a number\n");
    scanf("%d", &n);

    while (n != 0)
    {
        printf("You have entered %d as input\n Exiting now", n);
    }
    printf("%d", n);
}