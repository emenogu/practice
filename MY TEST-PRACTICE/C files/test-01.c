#include <stdio.h>

int main()
{
  int n;
    printf("Enter an integer\n", n);
    scanf("%d", &n);
while (n != 0)
  {
    printf("Enter an integer\n");
    scanf("%d", &n);
  }
  printf("You have done well and out of the loop");
}